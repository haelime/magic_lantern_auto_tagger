#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yorushika - Magic Lantern (幻燈) Auto Tagger
Automatically adds metadata and album cover to music files
"""

import os
import sys
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.flac import FLAC, Picture
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, APIC, TPE2

# Album Information
ALBUM_INFO = {
    'album': '幻燈',
    'album_artist': 'ヨルシカ',
    'artist': 'ヨルシカ',
    'year': '2023',
    'genre': 'J-Pop',
    'label': 'Universal Music'
}

# Track List (Digital Edition - 10 tracks)
TRACKS = {
    1: {'title': '都落ち', 'title_en': 'Miyakoochi'},
    2: {'title': 'ブレーメン', 'title_en': 'Bremen'},
    3: {'title': 'チノカテ', 'title_en': 'Chinokate'},
    4: {'title': '月に吠える', 'title_en': 'Tsuki ni Hoeru'},
    5: {'title': '451', 'title_en': '451'},
    6: {'title': '又三郎', 'title_en': 'Matasaburo'},
    7: {'title': '老人と海', 'title_en': 'Roujin to Umi'},
    8: {'title': '左右盲', 'title_en': 'Sayuu Mou'},
    9: {'title': 'アルジャーノン', 'title_en': 'Algernon'},
    10: {'title': '第一夜', 'title_en': 'Daiichiya'}
}

COVER_IMAGE = 'magic_lantern.jpeg'


def find_track_number(filename):
    """Extract track number from filename"""
    import re

    # Try to find track number at the beginning of filename
    match = re.match(r'^0?(\d+)', filename)
    if match:
        track_num = int(match.group(1))
        if 1 <= track_num <= 10:
            return track_num

    # Try to match with track titles
    filename_lower = filename.lower()
    for track_num, track_info in TRACKS.items():
        title = track_info['title']
        title_en = track_info['title_en'].lower()

        if title in filename or title_en in filename_lower:
            return track_num

    return None


def load_cover_image():
    """Load album cover image"""
    if not os.path.exists(COVER_IMAGE):
        print(f"⚠ Warning: Cover image '{COVER_IMAGE}' not found!")
        return None

    with open(COVER_IMAGE, 'rb') as f:
        return f.read()


def tag_mp3(filepath, track_num, cover_data):
    """Add metadata to MP3 file"""
    try:
        audio = MP3(filepath, ID3=ID3)

        # Add ID3 tag if not exists
        try:
            audio.add_tags()
        except:
            pass

        track_info = TRACKS[track_num]

        # Set metadata
        audio.tags.add(TIT2(encoding=3, text=track_info['title']))
        audio.tags.add(TPE1(encoding=3, text=ALBUM_INFO['artist']))
        audio.tags.add(TPE2(encoding=3, text=ALBUM_INFO['album_artist']))
        audio.tags.add(TALB(encoding=3, text=ALBUM_INFO['album']))
        audio.tags.add(TDRC(encoding=3, text=ALBUM_INFO['year']))
        audio.tags.add(TRCK(encoding=3, text=f"{track_num}/10"))

        # Add album cover
        if cover_data:
            audio.tags.add(
                APIC(
                    encoding=3,
                    mime='image/jpeg',
                    type=3,  # Cover (front)
                    desc='Cover',
                    data=cover_data
                )
            )

        audio.save()
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def tag_flac(filepath, track_num, cover_data):
    """Add metadata to FLAC file"""
    try:
        audio = FLAC(filepath)

        track_info = TRACKS[track_num]

        # Set metadata
        audio['TITLE'] = track_info['title']
        audio['ARTIST'] = ALBUM_INFO['artist']
        audio['ALBUMARTIST'] = ALBUM_INFO['album_artist']
        audio['ALBUM'] = ALBUM_INFO['album']
        audio['DATE'] = ALBUM_INFO['year']
        audio['TRACKNUMBER'] = str(track_num)
        audio['TRACKTOTAL'] = '10'
        audio['GENRE'] = ALBUM_INFO['genre']

        # Add album cover
        if cover_data:
            picture = Picture()
            picture.type = 3  # Cover (front)
            picture.mime = 'image/jpeg'
            picture.desc = 'Cover'
            picture.data = cover_data

            # Clear existing pictures
            audio.clear_pictures()
            audio.add_picture(picture)

        audio.save()
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def tag_m4a(filepath, track_num, cover_data):
    """Add metadata to M4A/MP4 file"""
    try:
        audio = MP4(filepath)

        track_info = TRACKS[track_num]

        # Set metadata
        audio['\xa9nam'] = track_info['title']
        audio['\xa9ART'] = ALBUM_INFO['artist']
        audio['aART'] = ALBUM_INFO['album_artist']
        audio['\xa9alb'] = ALBUM_INFO['album']
        audio['\xa9day'] = ALBUM_INFO['year']
        audio['trkn'] = [(track_num, 10)]
        audio['\xa9gen'] = ALBUM_INFO['genre']

        # Add album cover
        if cover_data:
            audio['covr'] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]

        audio.save()
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def process_file(filepath, cover_data):
    """Process a single music file"""
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    # Find track number
    track_num = find_track_number(filename)
    if track_num is None:
        print(f"⊘ Skipped: {filename} (could not determine track number)")
        return False

    track_info = TRACKS[track_num]
    print(f"♪ Processing: {filename}")
    print(f"  → Track {track_num}: {track_info['title']} ({track_info['title_en']})")

    # Tag file based on format
    success = False
    if ext == '.mp3':
        success = tag_mp3(filepath, track_num, cover_data)
    elif ext == '.flac':
        success = tag_flac(filepath, track_num, cover_data)
    elif ext in ['.m4a', '.mp4']:
        success = tag_m4a(filepath, track_num, cover_data)
    else:
        print(f"  ⊘ Unsupported format: {ext}")
        return False

    if success:
        print(f"  ✓ Successfully tagged!")

    return success


def main():
    print("=" * 70)
    print("  Yorushika - Magic Lantern (幻燈) Auto Tagger")
    print("=" * 70)
    print()

    # Get current directory
    current_dir = os.getcwd()
    print(f"Working directory: {current_dir}")
    print()

    # Load cover image
    print("Loading album cover...")
    cover_data = load_cover_image()
    if cover_data:
        print(f"✓ Loaded: {COVER_IMAGE} ({len(cover_data)} bytes)")
    print()

    # Find music files
    supported_formats = ['.mp3', '.flac', '.m4a', '.mp4']
    music_files = []

    for file in os.listdir(current_dir):
        if os.path.splitext(file)[1].lower() in supported_formats:
            music_files.append(file)

    if not music_files:
        print("✗ No music files found in current directory!")
        print(f"  Supported formats: {', '.join(supported_formats)}")
        input("\nPress Enter to exit...")
        return

    print(f"Found {len(music_files)} music file(s):")
    for file in music_files:
        print(f"  - {file}")
    print()

    # Process files
    print("Starting tagging process...")
    print("-" * 70)

    success_count = 0
    for file in music_files:
        filepath = os.path.join(current_dir, file)
        if process_file(filepath, cover_data):
            success_count += 1
        print()

    # Summary
    print("=" * 70)
    print(f"Completed! Successfully tagged {success_count}/{len(music_files)} file(s)")
    print("=" * 70)

    input("\nPress Enter to exit...")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)
