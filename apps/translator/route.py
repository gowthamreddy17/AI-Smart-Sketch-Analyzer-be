from fastapi import APIRouter
from pydantic import BaseModel
from googletrans import Translator

router = APIRouter()
translator = Translator()

class TranslationRequest(BaseModel):
    text: str
    from_lang: str = "auto"
    to_lang: str

@router.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        translated = translator.translate(request.text, src=request.from_lang, dest=request.to_lang)
        return {"original": request.text, "translated": translated.text, "from_lang": translated.src, "to_lang": translated.dest}
    except Exception as e:
        return {"error": str(e)}
