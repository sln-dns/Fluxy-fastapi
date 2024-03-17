from fastapi import APIRouter, HTTPException
import subprocess
import json
import os

router = APIRouter()

script_path = os.path.join(os.path.dirname(__file__), 'gtinProcessor.js')

def run_js_script(gtin):
    try:
        result = subprocess.run(['node', script_path, gtin], capture_output=True, text=True, check=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.stdout.strip():  # Проверяем, есть ли содержимое
            print("STDOUT:", result.stdout)
            return json.loads(result.stdout)
        else:
            raise ValueError("Пустой ответ от скрипта")
    except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError) as e:
        error_message = f"Ошибка при выполнении скрипта или обработке его вывода: {e}"
    print(error_message)
    raise HTTPException(status_code=500, detail=error_message)

@router.get("/gtin/{gtin}")
async def get_gtin(gtin: str):
    try:
        data = run_js_script(gtin)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))