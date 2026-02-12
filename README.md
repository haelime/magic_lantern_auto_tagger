# Yorushika - Magic Lantern Auto Tagger

> **Important:** Please read the [DISCLAIMER](DISCLAIMER.md) before using this software.

---

## 한국어 (Korean)

### 소개

ヨルシカ(Yorushika)의 앨범 **幻燈 (Magic Lantern / 2023)** 음악 파일에 메타데이터와 앨범 커버를 자동으로 입력하는 프로그램입니다.

Python 설치 없이 실행 파일만으로 바로 사용할 수 있습니다.

### 다운로드

**[Releases 페이지에서 다운로드](../../releases/latest)**

두 가지 방법 중 선택:

1. **ZIP 패키지 다운로드 (권장)**
   - `MagicLanternTagger-Windows.zip` 다운로드
   - 압축 해제하면 실행 파일과 앨범 커버가 함께 들어있음

2. **개별 파일 다운로드**
   - `MagicLanternTagger.exe` 다운로드
   - `magic_lantern.jpeg` 다운로드 (이 레포지토리에서)

### 사용 방법

1. **준비**
   - 음악 폴더에 `MagicLanternTagger.exe`와 `magic_lantern.jpeg` 복사
   - 두 파일이 음악 파일들과 같은 폴더에 있어야 합니다

2. **실행**
   - `MagicLanternTagger.exe` 더블클릭
   - 자동으로 모든 음악 파일 처리됨

3. **완료**
   - 처리된 파일은 메타데이터와 앨범 커버가 입력되어 있습니다

### 지원 포맷

- MP3
- FLAC
- M4A/MP4

### 지원 트랙리스트 (아트북 에디션 - 25곡)

**第1章：夏の肖像 (Chapter 1: Portrait of Summer)**
1. 夏の肖像 (Natsu no Shouzou)
2. 都落ち (Miyakoochi)
3. ブレーメン (Bremen)
4. チノカテ (Chinokate)
5. 雪国 (Yukiguni)
6. 月に吠える (Tsuki ni Hoeru)
7. 451
8. パドドゥ (Pas de Deux)
9. 又三郎 (Matasaburo)
10. 靴の花火 (Kutsu no Hanabi)
11. 老人と海 (Roujin to Umi)
12. さよならモルテン (Sayonara Molten)
13. いさな (Isana)
14. 左右盲 (Sayuu Mou)
15. アルジャーノン (Algernon)

**第2章：踊る動物 (Chapter 2: Dancing Animals)**
16. 第一夜 (Daiichiya)
17. 第二夜 (Dainiya)
18. 第三夜 (Daisanya)
19. 第四夜 (Daiyonya)
20. 第五夜 (Daigoya)
21. 第六夜 (Dairokuya)
22. 第七夜 (Dainanaya)
23. 第八夜 (Daihachiya)
24. 第九夜 (Daikyuuya)
25. 第十夜 (Daijuuya)

### 파일명 인식 패턴

프로그램은 다음과 같은 파일명을 자동으로 인식합니다:

- `01. 都落ち.mp3`
- `01 - 都落ち.flac`
- `01 Miyakoochi.mp3`
- `Track 01 - 都落ち.m4a`
- `都落ち.mp3` (트랙명만으로도 인식)
- `Miyakoochi.flac` (영문명으로도 인식)
- `Bremen.mp3`

### 문제 해결

**앨범 커버가 보이지 않는 경우**
- `magic_lantern.jpeg` 파일이 실행 파일과 같은 폴더에 있는지 확인
- 파일명이 정확히 일치하는지 확인

**특정 파일이 처리되지 않는 경우**
- 지원되는 포맷인지 확인 (MP3, FLAC, M4A, MP4)
- 파일이 읽기 전용이 아닌지 확인
- 다른 프로그램에서 파일을 사용 중이 아닌지 확인

**트랙 번호를 찾을 수 없다는 메시지**
- 파일명에 트랙 번호(01, 02 등) 또는 곡명이 포함되어 있는지 확인
- 위의 25개 트랙 목록에 있는 곡인지 확인

---

## English

### Introduction

This program automatically adds metadata and album cover to music files from Yorushika's album **幻燈 (Magic Lantern / 2023)**.

No Python installation required - just run the executable file.

### Download

**[Download from Releases page](../../releases/latest)**

Choose one of two options:

1. **ZIP Package Download (Recommended)**
   - Download `MagicLanternTagger-Windows.zip`
   - Extract to get both the executable and album cover

2. **Individual Files Download**
   - Download `MagicLanternTagger.exe`
   - Download `magic_lantern.jpeg` (from this repository)

### How to Use

1. **Preparation**
   - Copy `MagicLanternTagger.exe` and `magic_lantern.jpeg` to your music folder
   - Both files must be in the same folder as your music files

2. **Run**
   - Double-click `MagicLanternTagger.exe`
   - All music files will be processed automatically

3. **Done**
   - Processed files now have metadata and album cover embedded

### Supported Formats

- MP3
- FLAC
- M4A/MP4

### Supported Tracklist (Artbook Edition - 25 tracks)

**Chapter 1: Portrait of Summer (夏の肖像)**
1. Natsu no Shouzou (夏の肖像)
2. Miyakoochi (都落ち)
3. Bremen (ブレーメン)
4. Chinokate (チノカテ)
5. Yukiguni (雪国)
6. Tsuki ni Hoeru (月に吠える)
7. 451
8. Pas de Deux (パドドゥ)
9. Matasaburo (又三郎)
10. Kutsu no Hanabi (靴の花火)
11. Roujin to Umi (老人と海)
12. Sayonara Molten (さよならモルテン)
13. Isana (いさな)
14. Sayuu Mou (左右盲)
15. Algernon (アルジャーノン)

**Chapter 2: Dancing Animals (踊る動物)**
16. Daiichiya (第一夜)
17. Dainiya (第二夜)
18. Daisanya (第三夜)
19. Daiyonya (第四夜)
20. Daigoya (第五夜)
21. Dairokuya (第六夜)
22. Dainanaya (第七夜)
23. Daihachiya (第八夜)
24. Daikyuuya (第九夜)
25. Daijuuya (第十夜)

### Filename Recognition Patterns

The program automatically recognizes filenames like:

- `01. Miyakoochi.mp3`
- `01 - Bremen.flac`
- `01 Chinokate.mp3`
- `Track 01 - Yukiguni.m4a`
- `Miyakoochi.mp3` (track name only)
- `Bremen.flac` (English name only)

### Troubleshooting

**Album cover not showing**
- Check if `magic_lantern.jpeg` is in the same folder as the executable
- Verify the filename matches exactly

**Specific files not processed**
- Check if the format is supported (MP3, FLAC, M4A, MP4)
- Make sure the file is not read-only
- Close any programs that might be using the file

**Cannot determine track number message**
- Check if filename contains track number (01, 02, etc.) or track name
- Verify the song is one of the 25 tracks listed above

---

## 日本語 (Japanese)

### 紹介

ヨルシカのアルバム **幻燈 (Magic Lantern / 2023)** の音楽ファイルに、メタデータとアルバムカバーを自動的に追加するプログラムです。

Pythonのインストールは不要で、実行ファイルだけですぐに使用できます。

### ダウンロード

**[Releasesページからダウンロード](../../releases/latest)**

2つの方法から選択：

1. **ZIPパッケージダウンロード（推奨）**
   - `MagicLanternTagger-Windows.zip` をダウンロード
   - 解凍すると実行ファイルとアルバムカバーが含まれています

2. **個別ファイルダウンロード**
   - `MagicLanternTagger.exe` をダウンロード
   - `magic_lantern.jpeg` をダウンロード（このリポジトリから）

### 使用方法

1. **準備**
   - 音楽フォルダに `MagicLanternTagger.exe` と `magic_lantern.jpeg` をコピー
   - 両方のファイルが音楽ファイルと同じフォルダにある必要があります

2. **実行**
   - `MagicLanternTagger.exe` をダブルクリック
   - すべての音楽ファイルが自動的に処理されます

3. **完了**
   - 処理されたファイルにメタデータとアルバムカバーが追加されています

### サポート形式

- MP3
- FLAC
- M4A/MP4

### サポート対象トラックリスト（アートブックエディション - 25曲）

**第1章：夏の肖像**
1. 夏の肖像
2. 都落ち
3. ブレーメン
4. チノカテ
5. 雪国
6. 月に吠える
7. 451
8. パドドゥ
9. 又三郎
10. 靴の花火
11. 老人と海
12. さよならモルテン
13. いさな
14. 左右盲
15. アルジャーノン

**第2章：踊る動物**
16. 第一夜
17. 第二夜
18. 第三夜
19. 第四夜
20. 第五夜
21. 第六夜
22. 第七夜
23. 第八夜
24. 第九夜
25. 第十夜

### ファイル名認識パターン

プログラムは以下のようなファイル名を自動的に認識します：

- `01. 都落ち.mp3`
- `01 - ブレーメン.flac`
- `01 チノカテ.mp3`
- `Track 01 - 雪国.m4a`
- `都落ち.mp3`（トラック名のみでも認識）
- `Bremen.flac`（英語名でも認識）

### トラブルシューティング

**アルバムカバーが表示されない場合**
- `magic_lantern.jpeg` が実行ファイルと同じフォルダにあるか確認
- ファイル名が正確に一致しているか確認

**特定のファイルが処理されない場合**
- サポートされている形式か確認（MP3、FLAC、M4A、MP4）
- ファイルが読み取り専用でないか確認
- 他のプログラムでファイルを使用していないか確認

**トラック番号を判定できないというメッセージ**
- ファイル名にトラック番号（01、02など）または曲名が含まれているか確認
- 上記の25曲のリストにある曲か確認

---

## Credits

- **Album**: 幻燈 (Magic Lantern) - ヨルシカ (Yorushika)
- **Release**: April 5, 2023
- **Label**: Universal Music

---

Made with love for Yorushika fans
