import contextlib
import shutil
import os

from aiohttp.web import Application

from lona.logging import setup_logging
from lona.server import LonaServer


def collect_static(args):
    def _print(*print_args, **print_kwargs):
        if args.silent:
            return

        print(*print_args, **print_kwargs)

    def _rm(path):
        _print(f'rm -rf {path}')

        if args.dry_run:
            return

        if os.path.isdir(path):
            shutil.rmtree(path)

        else:
            os.unlink(path)

    def _mkdir(path):
        _print(f'mkdir -p {path}')

        if args.dry_run:
            return

        with contextlib.suppress(FileExistsError):
            os.makedirs(path)

    def _cp(source, destination):
        source_is_dir = os.path.isdir(source)

        if source_is_dir:
            _print(f'cp -r {source} {destination}')

        else:
            _print(f'cp {source} {destination}')

        if args.dry_run:
            return

        if source_is_dir:
            shutil.copytree(source, destination)

        else:
            shutil.copy(source, destination)

    # setup logging
    setup_logging(args)

    # setup server
    server = LonaServer(
        app=Application(),
        project_root=args.project_root,
        settings_paths=args.settings,
        settings_pre_overrides=args.settings_pre_overrides,
        settings_post_overrides=args.settings_post_overrides,
    )

    # check destination
    if not os.path.exists(args.destination):
        exit(f"'{args.destination}' does not exist")

    if not os.path.isdir(args.destination):
        exit(f"'{args.destination}' is no directory")

    # clean
    if args.clean:
        for name in os.listdir(args.destination):
            path = os.path.join(args.destination, name)
            _rm(path)

    # copy node static files
    for static_file in server._static_file_loader.static_files[::-1]:
        if not static_file.enabled:
            continue

        destination = os.path.join(
            args.destination,
            static_file.url,
        )

        _cp(static_file.path, destination)

    # copy static files from static directories
    for static_dir in server._static_file_loader.static_dirs[::-1]:
        for name in os.listdir(static_dir):
            source = os.path.join(static_dir, name)
            destination = os.path.join(args.destination, name)

            _cp(source, destination)

    # copy client
    for source_file in server._client_pre_compiler.get_source_files():
        source = server._client_pre_compiler.resolve_path(source_file)

        destination = os.path.join(
            args.destination,
            source_file,
        )

        _mkdir(os.path.dirname(destination))
        _cp(source, destination)
