#!/usr/bin/env python

import numpy as np


from DataSounds.sounds import build_scale, note_number, note_name


def test_build_scale_major():
    scale = build_scale('C', 'major', 1)
    assert any('is' in note for note in scale) is False


def test_build_scale_minor():
    scale = build_scale('A', 'minor', 1)
    assert any('is' in note for note in scale) is False


def test_build_scale_pentatonic():
    scale = build_scale('C', 'pentatonic', 1)
    assert scale == ['c', 'd', 'e', 'g', 'a']


def test_note_number():
    scale = build_scale('C', 'major', 1)
    assert all(note_number([1, 2, 3, 4], scale) == [0, 2, 4, 6])


def test_build_note_name():
    scale = build_scale('C', 'major', 1)
    notes = note_number([1, 2, 3, 4, np.nan], scale)
    assert [note_name(x, scale) for x in notes] == ['c', 'e', 'g', 'b', 'r']