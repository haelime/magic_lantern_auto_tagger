# Release Guide

이 문서는 관리자가 새 버전을 릴리스하는 방법을 설명합니다.

## 🚀 새 버전 릴리스하기

### 1. 코드 변경사항 커밋

```bash
git add .
git commit -m "feat: 새로운 기능 추가"
git push origin main
```

### 2. 버전 태그 생성 및 푸시

```bash
# 버전 번호는 Semantic Versioning 사용 (v1.0.0, v1.1.0, v2.0.0 등)
git tag v1.0.0

# 태그에 메시지 추가 (선택사항)
git tag -a v1.0.0 -m "Release version 1.0.0"

# 태그를 원격 저장소에 푸시
git push origin v1.0.0
```

### 3. 자동 빌드 및 릴리스

태그를 푸시하면 자동으로:

1. **GitHub Actions 워크플로우 실행**
   - Windows 환경에서 Python 설치
   - 의존성 설치
   - PyInstaller로 .exe 빌드
   - ZIP 패키지 생성

2. **GitHub Release 자동 생성**
   - `MagicLanternTagger.exe` 업로드
   - `MagicLanternTagger-Windows.zip` 업로드
   - 릴리스 노트 자동 생성

3. **사용자에게 배포**
   - Releases 페이지에서 다운로드 가능
   - 링크: `https://github.com/<username>/<repo>/releases/latest`

### 4. 릴리스 확인

1. [Actions 탭](../../actions)에서 워크플로우 실행 상태 확인
2. [Releases 페이지](../../releases)에서 새 릴리스 확인
3. 다운로드 테스트

## 📝 버전 번호 규칙 (Semantic Versioning)

```
v<Major>.<Minor>.<Patch>

예시:
- v1.0.0 - 첫 릴리스
- v1.0.1 - 버그 수정
- v1.1.0 - 새 기능 추가 (하위 호환)
- v2.0.0 - 주요 변경사항 (하위 호환 깨짐)
```

## 🔧 수동 릴리스 (비상시)

GitHub Actions가 실패하거나 수동 릴리스가 필요한 경우:

### 방법 1: 로컬 빌드 후 수동 업로드

```bash
# 로컬에서 빌드
build.bat

# GitHub Releases 페이지에서 수동으로 릴리스 생성
# dist/MagicLanternTagger.exe 파일 업로드
```

### 방법 2: GitHub Actions 수동 실행

1. [Actions 탭](../../actions) 이동
2. "Build and Release" 워크플로우 선택
3. "Run workflow" 버튼 클릭
4. 브랜치 선택 후 실행

## ⚠️ 주의사항

- **태그는 신중하게 푸시**: 태그를 푸시하면 자동으로 릴리스가 생성됩니다
- **버전 번호 중복 금지**: 이미 존재하는 버전 번호는 사용하지 마세요
- **테스트 후 릴리스**: 로컬에서 충분히 테스트한 후 릴리스하세요
- **CHANGELOG 업데이트**: 주요 변경사항은 CHANGELOG.md에 기록하세요 (선택사항)

## 🗑️ 릴리스 삭제

실수로 릴리스를 만든 경우:

1. [Releases 페이지](../../releases)에서 해당 릴리스 삭제
2. 태그 삭제:
   ```bash
   # 로컬 태그 삭제
   git tag -d v1.0.0

   # 원격 태그 삭제
   git push origin --delete v1.0.0
   ```

## 📋 체크리스트

릴리스 전 확인사항:

- [ ] 코드가 정상적으로 동작하는가?
- [ ] 로컬에서 빌드 테스트를 했는가?
- [ ] README.md가 최신 정보를 담고 있는가?
- [ ] 버전 번호가 적절한가?
- [ ] 모든 변경사항이 커밋되었는가?
- [ ] main 브랜치에 푸시했는가?

모든 체크가 완료되면:
```bash
git tag v1.0.0
git push origin v1.0.0
```
