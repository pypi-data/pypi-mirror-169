# MedicalImage

## Build 환경
* `medical-image` 프로젝트 권한이 있는 `pypi` 계정 필요 (김화평 팀장에게 문의)
* `dc-xr-03` 띄울 때 경로에 맞춰 volumes에 `- ../../medical-image:/medical-image` 추가
* 동일 버전 업로드는 오류가 남! 반드시 버전 업 후 업로드 해야 함!

## Build
```
docker exec -it dc-xr-03 /bin/bash
cd /medical-image
pip install twine
rm -r build dist medical_image.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
```