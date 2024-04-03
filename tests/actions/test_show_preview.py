from pro_filer.actions.main_actions import show_preview


def test_show_preview_with_data(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 3 files and 2 directories" in captured.out
    assert "Found 3 files and 2 directories" in captured.out
    assert f'First 5 files: {context["all_files"][:5]}' in captured.out
    assert f'First 5 directories: {context["all_dirs"][:5]}' in captured.out


def test_show_preview_no_data(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 0 files and 0 directories" in captured.out


def test_show_preview_exceeds_limit(capsys):
    context = {
        "all_files": ["file1", "file2", "file3", "file4", "file5", "file6"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 6 files and 6 directories" in captured.out
    assert f'First 5 files: {context["all_files"][:5]}' in captured.out
    assert f'First 5 directories: {context["all_dirs"][:5]}' in captured.out
