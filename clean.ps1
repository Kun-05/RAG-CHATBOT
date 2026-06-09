Write-Host "Cleaning project RAG..." -ForegroundColor Cyan

if (Test-Path -Path "db\vector_db.json") {
    Remove-Item -Path "db\vector_db.json" -Force
    Write-Host "Cleaned vector_db.json" -ForegroundColor Green
}

# Dọn dẹp Python cache (__pycache__ và .pyc)
Get-ChildItem -Path . -Include "__pycache__" -Recurse -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Include "*.pyc" -Recurse -File | Remove-Item -Force
Write-Host "Cleaned Python cache" -ForegroundColor Green

Write-Host "Completed!" -ForegroundColor Yellow