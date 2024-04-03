import os
from datetime import datetime

import pytest
from pro_filer.actions.main_actions import show_details


def test_show_details_file_exists(capsys):
    file_path = "/home/trybe/Downloads/Trybe_logo.png"
    context = {"base_path": file_path}
    if os.path.exists(file_path):
        show_details(context)
        captured = capsys.readouterr()
        assert f"File name: {file_path.split('/')[-1]}" in captured.out
        assert (
            f"""File size in bytes:
        {os.path.getsize(file_path)}"""
            in captured.out
        )
        assert "File type: file" in captured.out
        _, file_extension = os.path.splitext(file_path)
        file_extension_msg = "File extension: " + (
            file_extension or "[no extension]"
        )
        assert file_extension_msg in captured.out
        mod_date = datetime.fromtimestamp(
            os.path.getmtime(file_path)
        ).strftime("%Y-%m-%d")
        assert f"Last modified date: {mod_date}" in captured.out
    else:
        assert "File 'Trybe_logo.png' does not exist"


def test_show_details_file_not_exists(capsys):
    file_path = "/home/trybe/????"
    context = {"base_path": file_path}
    show_details(context)
    captured = capsys.readouterr()
    assert "File '????' does not exist" in captured.out


def test_show_details_directory_exists(capsys):
    dir_path = "/home/trybe/Downloads"
    context = {"base_path": dir_path}

    if os.path.exists(dir_path):
        show_details(context)
        captured = capsys.readouterr()
        assert f"File name: {dir_path.split('/')[-1]}" in captured.out
        assert (
            f"""File size in bytes: {
            os.path.getsize(dir_path)
            }"""
            in captured.out
        )
        assert "File type: directory" in captured.out
        assert "File extension: [no extension]" in captured.out
        mod_date = datetime.fromtimestamp(os.path.getmtime(dir_path)).strftime(
            "%Y-%m-%d"
        )
        assert f"Last modified date: {mod_date}" in captured.out
    else:
        assert "Directory 'Downloads' does not exist"


@pytest.mark.xfail
def test_show_details_file_without_extension(capsys):
    file_path = "/home/trybe/Downloads/file_without_extension"
    context = {"base_path": file_path}
    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out
    assert "File 'file_without_extension' does not exist" in captured.out


@pytest.mark.xfail
def test_show_details_file_with_timestamp_creation_date(capsys):
    file_path = "/home/trybe/Downloads/file_with_timestamp_creation_date"
    context = {"base_path": file_path}
    show_details(context)
    captured = capsys.readouterr()
    mod_date_expected = "Last modified date: 2024-04-05"
    assert mod_date_expected not in captured.out
    assert f"File '{file_path}' does not exist" in captured.out
