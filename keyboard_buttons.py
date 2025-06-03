from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📢 Elon berish"),
            
        ],
        

        [  
            KeyboardButton(text="Biz haqimizda🔥"),
             KeyboardButton(text="Admin bilan bog'lanish👨🏻‍💻"),
        ],
        
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang"
)
