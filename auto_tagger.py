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
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TRCK, APIC, TPE2, TCOM, TCON

# Album Information
ALBUM_INFO = {
    'album': '幻燈',
    'album_artist': 'ヨルシカ',
    'artist': 'ヨルシカ',
    'year': '2023',
    'genre': 'J-Pop',
    'composer': 'n-buna',
    'label': 'Universal Music'
}

# Track List (Artbook Edition - 25 tracks)
# Chapter 1: Portrait of Summer (夏の肖像)
# Chapter 2: Dancing Animals (踊る動物)
TRACKS = {
    # Chapter 1: Portrait of Summer
    1: {'title': '夏の肖像', 'title_en': 'Natsu no Shouzou'},
    2: {'title': '都落ち', 'title_en': 'Miyakoochi'},
    3: {'title': 'ブレーメン', 'title_en': 'Bremen'},
    4: {'title': 'チノカテ', 'title_en': 'Chinokate'},
    5: {'title': '雪国', 'title_en': 'Yukiguni'},
    6: {'title': '月に吠える', 'title_en': 'Tsuki ni Hoeru'},
    7: {'title': '451', 'title_en': '451'},
    8: {'title': 'パドドゥ', 'title_en': 'Pas de Deux'},
    9: {'title': '又三郎', 'title_en': 'Matasaburo'},
    10: {'title': '靴の花火', 'title_en': 'Kutsu no Hanabi'},
    11: {'title': '老人と海', 'title_en': 'Roujin to Umi'},
    12: {'title': 'さよならモルテン', 'title_en': 'Sayonara Molten'},
    13: {'title': 'いさな', 'title_en': 'Isana'},
    14: {'title': '左右盲', 'title_en': 'Sayuu Mou'},
    15: {'title': 'アルジャーノン', 'title_en': 'Algernon'},
    # Chapter 2: Dancing Animals
    16: {'title': '第一夜', 'title_en': 'Daiichiya'},
    17: {'title': '第二夜', 'title_en': 'Dainiya'},
    18: {'title': '第三夜', 'title_en': 'Daisanya'},
    19: {'title': '第四夜', 'title_en': 'Daiyonya'},
    20: {'title': '第五夜', 'title_en': 'Daigoya'},
    21: {'title': '第六夜', 'title_en': 'Dairokuya'},
    22: {'title': '第七夜', 'title_en': 'Dainanaya'},
    23: {'title': '第八夜', 'title_en': 'Daihachiya'},
    24: {'title': '第九夜', 'title_en': 'Daikyuuya'},
    25: {'title': '第十夜', 'title_en': 'Daijuuya'}
}

COVER_IMAGE = 'magic_lantern.jpeg'


def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def find_track_number(filename):
    """Extract track number from filename"""
    import re

    # Try to find track number at the beginning of filename
    match = re.match(r'^0?(\d+)', filename)
    if match:
        track_num = int(match.group(1))
        if 1 <= track_num <= 25:
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
    # Get the correct path for the bundled image (works for both dev and PyInstaller)
    image_path = get_resource_path(COVER_IMAGE)

    print(f"🔍 Debug: Looking for cover image at: {image_path}")
    print(f"🔍 Debug: Current working directory: {os.getcwd()}")

    # Check if running as PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        print(f"🔍 Debug: Running as PyInstaller bundle. _MEIPASS = {sys._MEIPASS}")
    else:
        print(f"🔍 Debug: Running as normal Python script")

    if not os.path.exists(image_path):
        print(f"⚠ Warning: Cover image '{COVER_IMAGE}' not found at {image_path}!")
        # List files in the directory for debugging
        try:
            dir_path = os.path.dirname(image_path) or '.'
            print(f"🔍 Debug: Files in {dir_path}:")
            for f in os.listdir(dir_path)[:10]:  # Show first 10 files
                print(f"  - {f}")
        except Exception as e:
            print(f"  Could not list directory: {e}")
        return None

    print(f"✓ Found cover image! Size: {os.path.getsize(image_path)} bytes")
    with open(image_path, 'rb') as f:
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

        # Debug: Check existing APIC frames before deletion
        existing_apic = audio.tags.getall('APIC')
        print(f"  🔍 Before: Found {len(existing_apic)} existing APIC frame(s)")

        # Delete existing tags and set new metadata
        audio.tags.delall('TIT2')
        audio.tags.add(TIT2(encoding=3, text=track_info['title']))

        audio.tags.delall('TPE1')
        audio.tags.add(TPE1(encoding=3, text=ALBUM_INFO['artist']))

        audio.tags.delall('TPE2')
        audio.tags.add(TPE2(encoding=3, text=ALBUM_INFO['album_artist']))

        audio.tags.delall('TALB')
        audio.tags.add(TALB(encoding=3, text=ALBUM_INFO['album']))

        audio.tags.delall('TDRC')
        audio.tags.add(TDRC(encoding=3, text=ALBUM_INFO['year']))

        audio.tags.delall('TRCK')
        audio.tags.add(TRCK(encoding=3, text=f"{track_num}/25"))

        audio.tags.delall('TCON')
        audio.tags.add(TCON(encoding=3, text=ALBUM_INFO['genre']))

        audio.tags.delall('TCOM')
        audio.tags.add(TCOM(encoding=3, text=ALBUM_INFO['composer']))

        # Delete existing album cover and add new one
        if cover_data:
            # Delete ALL existing APIC frames
            audio.tags.delall('APIC')
            print(f"  🔍 Deleted all APIC frames")

            # Add new album cover
            audio.tags.add(
                APIC(
                    encoding=3,
                    mime='image/jpeg',
                    type=3,  # Cover (front)
                    desc='Cover',
                    data=cover_data
                )
            )
            print(f"  ✓ Added new album cover ({len(cover_data)} bytes)")

        # Save with ID3v2.3 for better compatibility
        audio.save(v2_version=3)
        print(f"  💾 Saved with ID3v2.3 format")

        # Verify: Read file again and check if cover was saved
        verify_audio = MP3(filepath, ID3=ID3)
        verify_apic = verify_audio.tags.getall('APIC')
        print(f"  ✅ Verification: Found {len(verify_apic)} APIC frame(s) after save")
        if verify_apic:
            print(f"  ✅ Cover size in file: {len(verify_apic[0].data)} bytes")

        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def tag_flac(filepath, track_num, cover_data):
    """Add metadata to FLAC file"""
    try:
        audio = FLAC(filepath)

        track_info = TRACKS[track_num]

        # Debug: Check existing pictures
        existing_pics = audio.pictures
        print(f"  🔍 Before: Found {len(existing_pics)} existing picture(s)")

        # Set metadata
        audio['TITLE'] = track_info['title']
        audio['ARTIST'] = ALBUM_INFO['artist']
        audio['ALBUMARTIST'] = ALBUM_INFO['album_artist']
        audio['ALBUM'] = ALBUM_INFO['album']
        audio['DATE'] = ALBUM_INFO['year']
        audio['TRACKNUMBER'] = str(track_num)
        audio['TRACKTOTAL'] = '25'
        audio['GENRE'] = ALBUM_INFO['genre']
        audio['COMPOSER'] = ALBUM_INFO['composer']

        # Add album cover
        if cover_data:
            # Clear existing pictures
            audio.clear_pictures()
            print(f"  🔍 Cleared all existing pictures")

            picture = Picture()
            picture.type = 3  # Cover (front)
            picture.mime = 'image/jpeg'
            picture.desc = 'Cover'
            picture.data = cover_data
            audio.add_picture(picture)
            print(f"  ✓ Added new album cover ({len(cover_data)} bytes)")

        audio.save()
        print(f"  💾 Saved FLAC file")

        # Verify
        verify_audio = FLAC(filepath)
        verify_pics = verify_audio.pictures
        print(f"  ✅ Verification: Found {len(verify_pics)} picture(s) after save")
        if verify_pics:
            print(f"  ✅ Cover size in file: {len(verify_pics[0].data)} bytes")

        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def tag_m4a(filepath, track_num, cover_data):
    """Add metadata to M4A/MP4 file"""
    try:
        audio = MP4(filepath)

        track_info = TRACKS[track_num]

        # Debug: Check existing cover
        existing_cover = audio.get('covr', [])
        print(f"  🔍 Before: Found {len(existing_cover)} existing cover(s)")

        # Set metadata
        audio['\xa9nam'] = track_info['title']
        audio['\xa9ART'] = ALBUM_INFO['artist']
        audio['aART'] = ALBUM_INFO['album_artist']
        audio['\xa9alb'] = ALBUM_INFO['album']
        audio['\xa9day'] = ALBUM_INFO['year']
        audio['trkn'] = [(track_num, 25)]
        audio['\xa9gen'] = ALBUM_INFO['genre']
        audio['\xa9wrt'] = ALBUM_INFO['composer']

        # Add album cover
        if cover_data:
            # Delete existing cover and set new one
            if 'covr' in audio:
                del audio['covr']
                print(f"  🔍 Deleted existing cover")

            audio['covr'] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]
            print(f"  ✓ Added new album cover ({len(cover_data)} bytes)")

        audio.save()
        print(f"  💾 Saved M4A/MP4 file")

        # Verify
        verify_audio = MP4(filepath)
        verify_cover = verify_audio.get('covr', [])
        print(f"  ✅ Verification: Found {len(verify_cover)} cover(s) after save")
        if verify_cover:
            print(f"  ✅ Cover size in file: {len(verify_cover[0])} bytes")

        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
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
