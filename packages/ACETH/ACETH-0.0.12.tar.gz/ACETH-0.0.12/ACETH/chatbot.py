import emoji,os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import logging
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import warnings

warnings.filterwarnings("ignore")

class chatbot:
    def __init__(self,emoji=True):
        self.emoji = emoji
        print('Loading model and other dependecies..',sep='')
        logging.disable_progress_bar()
        loc = os.path.dirname(__file__)
        self.token_chat = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model_chat = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        with open(loc+'/data/token_emoji.pkl','rb') as f:
            self.token_em = pickle.load(f)
        with open(loc+'/data/encoder_emoji.pkl','rb') as f:
            self.encod_em = pickle.load(f)

        self.model_emoji = load_model(loc+'/data/emoji_model.h5')
        print('Model and tokenizer is loaded')
        self.main()

    def addEmoji(self,text):
        x = pad_sequences(self.token_em.texts_to_sequences([text]),maxlen=30)
        y_hot = self.model_emoji.predict([x],verbose=0)[0]
        w_sum = sum(y_hot)
        sort = list(sorted(y_hot))
        dummy = []
        count = 0
        for i in sort:
            count+=i
            dummy.append(count)
        sort = dummy
        r = np.random.uniform(0,1)
        y = np.argmax(y_hot)
        for i,w in enumerate(sort[:-1]):
            if r <= w:
                y = i
                break
        y = self.encod_em.inverse_transform([y])[0]

      
        text = emoji.emojize(f'{text} :{y}:')
        return text
    def main(self): 
        self.step = 0
        torch.manual_seed(42)
        last = '-1'
        while 1:
            user_text = input('>> User : ')
            if user_text == ':q':
                self.step = 0
                break
            new_user_input_ids = self.token_chat.encode(user_text + self.token_chat.eos_token, return_tensors='pt')
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if self.step > 0 else new_user_input_ids
            chat_history_ids = self.model_chat.generate(bot_input_ids,max_length=1000, pad_token_id=self.token_chat.eos_token_id, top_k=50, top_p = 0.95, do_sample=True)

            text = self.token_chat.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            
            if last in text or text in last or 'bye' in text or 'ok' in text or 'alright' in text:
                last = '-1'
                step = 0
            else:
                last = text
            if self.emoji and ':D' not in text and ':)' not in text:
                text = self.addEmoji(text)
            self.step+=1
            
            print('ACE chatbot : {}'.format(text))
        s = input("You wanna talk to me again? (Y/n)")
        if s == 'Y':
            self.main()
            return
        
        
