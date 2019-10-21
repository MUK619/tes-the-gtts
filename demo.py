import wikipedia as wiki
from gtts import gTTS
import os
# import webbrowser as wb
# result = wiki.search('PYTHON')
result = wiki.summary("Java",sentences=1)
print(result)

result_mp3 = gTTS(text = result, lang='en', slow=False)
result_mp3.save(result[:10]+".mp3")
os.startfile(
    os.path.join(
        os.getcwd(),
        result[:10]+'.mp3'
    )
)