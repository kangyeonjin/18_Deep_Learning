from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
from enum import Enum
# import asyncio

#모델 load
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

#tokenizer load
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

app =  FastAPI()

class Language(str, Enum):
    Arabic = "ar_AR"
    Czech = "cs_CZ"
    German = "de_DE"
    English = "en_XX"
    Spanish = "es_XX"
    Estonian = "et_EE"
    Finnish = "fi_FI"
    French = "fr_XX"
    Gujarati = "gu_IN"
    Hindi = "hi_IN"
    Italian = "it_IT"
    Japanese = "ja_XX"
    Kazakh = "kk_KZ"
    Korean = "ko_KR"
    Lithuanian = "lt_LT"
    Latvian = "lv_LV"
    Burmese = "my_MM"
    Nepali = "ne_NP"
    Dutch = "nl_XX"
    Romanian = "ro_RO"
    Russian = "ru_RU"
    Sinhala = "si_LK"
    Turkish = "tr_TR"
    Vietnamese = "vi_VN"
    Chinese = "zh_CN"
    Afrikaans = "af_ZA"
    Azerbaijani = "az_AZ"
    Bengali = "bn_IN"
    Persian = "fa_IR"
    Hebrew = "he_IL"
    Croatian = "hr_HR"
    Indonesian = "id_ID"
    Georgian = "ka_GE"
    Khmer = "km_KH"
    Macedonian = "mk_MK"
    Malayalam = "ml_IN"
    Mongolian = "mn_MN"
    Marathi = "mr_IN"
    Polish = "pl_PL"
    Pashto = "ps_AF"
    Portuguese = "pt_XX"
    Swedish = "sv_SE"
    Swahili = "sw_KE"
    Tamil = "ta_IN"
    Telugu = "te_IN"
    Thai = "th_TH"
    Tagalog = "tl_XX"
    Ukrainian = "uk_UA"
    Urdu = "ur_PK"
    Xhosa = "xh_ZA"
    Galician = "gl_ES"
    Slovene = "sl_SI"

class TranslationRequest(BaseModel):
    text : str
    lang : Language
    
@app.get("/")
async def read_root():
    return {"message": "Hello World"}    
    
@app.post("/translate")
async def translate(request : TranslationRequest):
    
    #전처리
    #한글 토큰화
    tokenizer.src_lang = "ko_KR"
    
    encoded_ko = tokenizer(request.text, return_tensors="pt")
    
    #추론
    generated_tokens = model.generate(
        **encoded_ko,
        forced_bos_token_id = tokenizer.lang_code_to_id[request.lang]
    )
    
    #후처리
    #번역결과 decoding
    translate_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    print(translate_text)
    
    return {"translated_text" : translate_text[0]}

