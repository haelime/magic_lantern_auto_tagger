# Yorushika - Magic Lantern (幻燈) Auto Tagger

ヨルシカ(Yorushika)의 앨범 **幻燈 (Magic Lantern / 2023)** 음악 파일에 메타데이터와 앨범 커버를 자동으로 입력하는 프로그램입니다.

## ✨ 특징

- 🎵 **자동 트랙 인식**: 파일명에서 트랙 번호 또는 곡명을 자동으로 인식
- 🎨 **앨범 커버 삽입**: `magic_lantern.jpeg` 이미지를 자동으로 삽입
- 📝 **완전한 메타데이터**: 아티스트, 앨범명, 발매연도, 트랙 번호 등 모든 정보 입력
- 💿 **다양한 포맷 지원**: MP3, FLAC, M4A/MP4 파일 지원
- 🚀 **원클릭 실행**: Python 설치 없이 .exe 파일만으로 실행 가능

## 📋 지원 트랙리스트 (아트북 에디션 - 25곡)

### 第1章：夏の肖像 (Chapter 1: Portrait of Summer)
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

### 第2章：踊る動物 (Chapter 2: Dancing Animals)
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

## 🚀 빠른 시작

### 📦 다운로드 (권장)

**[→ Releases 페이지에서 다운로드](../../releases/latest)**

1. **ZIP 패키지 다운로드** (가장 쉬움)
   - `MagicLanternTagger-Windows.zip` 다운로드
   - 압축 해제하면 실행 파일과 앨범 커버가 함께 들어있음

2. **또는 개별 파일 다운로드**
   - `MagicLanternTagger.exe` 다운로드
   - `magic_lantern.jpeg` 다운로드 (레포지토리에서)

### 💿 사용 방법

1. **음악 폴더에 복사**
   ```
   내음악폴더/
   ├── MagicLanternTagger.exe    ← 다운로드한 실행 파일
   ├── magic_lantern.jpeg         ← 앨범 커버 이미지
   ├── 01. 都落ち.mp3
   ├── 02. ブレーメン.mp3
   └── ...
   ```

2. **실행**
   - `MagicLanternTagger.exe` 더블클릭
   - 자동으로 모든 음악 파일 처리
   - 완료! ✨

> ⚠️ **중요**:
> - `magic_lantern.jpeg`와 음악 파일들이 같은 폴더에 있어야 합니다
> - **Python 설치 불필요** - .exe 파일만으로 바로 실행됩니다!

## 📖 사용법 상세

### 파일명 인식 패턴

프로그램은 다음과 같은 파일명 패턴을 자동으로 인식합니다:

```
✅ 인식 가능한 파일명 예시:
- 01. 都落ち.mp3
- 01 - 都落ち.flac
- 01 Miyakoochi.mp3
- Track 01 - 都落ち.m4a
- 都落ち.mp3 (트랙명만으로도 인식)
- Miyakoochi.flac (영문명으로도 인식)
- Bremen.mp3 (영문명으로도 인식)
```

### 입력되는 메타데이터

각 파일에 다음 정보가 자동으로 입력됩니다:

- **제목**: 각 트랙의 일본어 제목
- **아티스트**: ヨルシカ (Yorushika)
- **앨범 아티스트**: ヨルシカ
- **앨범**: 幻燈
- **발매연도**: 2023
- **트랙 번호**: X/10
- **장르**: J-Pop
- **앨범 커버**: magic_lantern.jpeg

## 🔧 개발자용

### Python 스크립트 직접 실행

빌드하지 않고 Python으로 직접 실행하려면:

```bash
# 방법 1: uv 사용 (권장 - 매우 빠름!)
uv pip install -r requirements.txt
python auto_tagger.py

# 방법 2: pip 사용 (전통적인 방법)
pip install -r requirements.txt
python auto_tagger.py
```

> 💡 **Tip**: [uv](https://github.com/astral-sh/uv)는 Rust로 작성된 초고속 Python 패키지 관리 도구입니다. pip보다 10-100배 빠릅니다!

### 로컬에서 직접 빌드하기

GitHub Actions 대신 로컬에서 빌드하려면:

#### 필요사항
- Windows 10/11
- Python 3.8 이상 ([다운로드](https://www.python.org/downloads/))
  - ⚠️ 설치 시 **"Add Python to PATH"** 체크 필수!
- uv (선택사항, 하지만 강력 권장)

#### 빌드 실행

**방법 1: 배치 파일 사용 (가장 쉬움)**
```bash
build.bat
```
> `build.bat`는 uv가 없으면 자동으로 설치한 후 빌드합니다!

**방법 2: uv로 수동 빌드 (빠름)**
```bash
# uv 설치 (Windows)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 의존성 설치 및 빌드
uv pip install -r requirements.txt
pyinstaller --onefile --name "MagicLanternTagger" --add-data "magic_lantern.jpeg;." auto_tagger.py
```

**방법 3: pip로 수동 빌드 (전통적)**
```bash
pip install -r requirements.txt
pyinstaller --onefile --name "MagicLanternTagger" --add-data "magic_lantern.jpeg;." auto_tagger.py
```

빌드된 파일은 `dist\MagicLanternTagger.exe`에 생성됩니다.

### 자동 빌드 (GitHub Actions)

이 프로젝트는 GitHub Actions를 통해 자동으로 빌드됩니다:

- **트리거**: 태그 푸시 시 (`v1.0.0` 같은 형식)
- **빌드 도구**: uv를 사용한 초고속 빌드 ⚡
- **결과물**: Windows .exe 파일
- **배포**: GitHub Releases에 자동 업로드

새 버전 릴리스 방법:
```bash
git tag v1.0.0
git push origin v1.0.0
```

> 💡 GitHub Actions에서는 uv를 사용하여 의존성을 매우 빠르게 설치합니다 (pip 대비 10-100배 빠름)

### 프로젝트 구조

```
magic_lantern_auto_tagger/
├── .github/
│   └── workflows/
│       └── build-and-release.yml  # GitHub Actions 워크플로우
├── auto_tagger.py                # 메인 스크립트
├── requirements.txt              # Python 의존성
├── build.bat                     # 로컬 빌드 스크립트
├── magic_lantern.jpeg            # 앨범 커버 이미지
├── .gitignore
└── README.md                     # 이 파일
```

### 의존성

- **mutagen**: 음악 파일 메타데이터 편집
- **pyinstaller**: Python 스크립트를 .exe로 변환

## ❓ 문제 해결

### "Python is not installed or not in PATH" 에러
- Python 설치 시 "Add Python to PATH" 옵션을 체크했는지 확인
- 명령 프롬프트에서 `python --version` 실행해서 확인

### "Cover image not found" 경고
- `magic_lantern.jpeg` 파일이 실행 파일과 같은 폴더에 있는지 확인
- 파일명이 정확히 일치하는지 확인 (대소문자 구분)

### "Could not determine track number" 메시지
- 파일명에 트랙 번호(01, 02 등) 또는 곡명이 포함되어 있는지 확인
- 지원되는 10개 트랙 이외의 파일일 수 있음

### 특정 파일이 처리되지 않음
- 지원되는 포맷인지 확인 (MP3, FLAC, M4A, MP4)
- 파일이 읽기 전용이 아닌지 확인
- 다른 프로그램에서 파일을 사용 중이 아닌지 확인

## 📄 라이센스

이 프로그램은 개인적인 사용을 위해 제작되었습니다.
앨범 커버와 메타데이터의 저작권은 ヨルシカ(Yorushika) 및 Universal Music에 있습니다.

## 🙏 크레딧

- **앨범**: 幻燈 (Magic Lantern) - ヨルシカ (Yorushika)
- **발매**: 2023년 4월 5일
- **레이블**: Universal Music

---

Made with ❤️ for Yorushika fans
