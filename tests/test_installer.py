from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import install


class InstallerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text("---\nname: opervia\n---\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_install_and_update_owned_destination(self) -> None:
        destination = self.root / "skills" / "opervia"
        install.install_skill(self.source, destination)
        marker = json.loads((destination / install.MARKER_NAME).read_text(encoding="utf-8"))
        self.assertEqual(install.PACKAGE_ID, marker["package"])

        (self.source / "reference.md").write_text("updated", encoding="utf-8")
        install.install_skill(self.source, destination)
        self.assertEqual("updated", (destination / "reference.md").read_text(encoding="utf-8"))

    def test_refuses_to_overwrite_unmanaged_destination(self) -> None:
        destination = self.root / "skills" / "opervia"
        destination.mkdir(parents=True)
        (destination / "personal.md").write_text("keep", encoding="utf-8")

        with self.assertRaises(RuntimeError):
            install.install_skill(self.source, destination)

        self.assertEqual("keep", (destination / "personal.md").read_text(encoding="utf-8"))

    def test_auto_detects_existing_agents_and_falls_back_to_generic(self) -> None:
        home = self.root / "home"
        (home / ".codex").mkdir(parents=True)
        (home / ".claude").mkdir()
        self.assertEqual(["codex", "claude"], install.detect_agents(home, {}))
        self.assertEqual(["generic"], install.detect_agents(self.root / "empty", {}))


if __name__ == "__main__":
    unittest.main()
