from pathlib import Path

from migrate_code.migration import Migration


def load_migration(file: Path) -> Migration:
    code = file.read_text()
    globals_: dict = {}
    exec(code, globals_)
    if not ("migration" in globals_ or "m" in globals_):
        raise RuntimeError("migration.py must define a 'migration' or 'm' variable.")
    if "migration" in globals_:
        migration = globals_["migration"]
    else:
        migration = globals_["m"]
    if not isinstance(migration, Migration):
        raise TypeError(
            "Migration variable should be a 'migrate_code.migration.Migration' "
            f"but got instead {type(migration)}"
        )
    return migration
