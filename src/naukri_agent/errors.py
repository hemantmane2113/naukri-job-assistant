"""Errors that mean "you have not set this up yet", so the command line can say so in one line instead of a traceback."""


class ConfigFileNotFound(FileNotFoundError):
    """A personal config file (candidate profile, master resume, resume list) does not exist yet.

    The message already says which file and how to create it. It stays a FileNotFoundError so anything that catches that still
    works."""
