from transitions.extensions import GraphMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message

from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
pet=""
class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "home"
    def on_enter_user(self, event):
        text = 'home'
        send_text_message(event.reply_token,text)
    def is_going_to_care(self, event):
        text = event.message.text
        return text.lower() == "care"

    def is_going_to_adapt(self, event):
        text = event.message.text
        return text.lower() == "adapt"

    def on_enter_care(self, event):
        title = '請問你比較想知道狗狗還是貓咪的照顧資訊'
        text = '『狗狗』還是『貓咪』'
        btn = [
            MessageTemplateAction(
                label='狗狗',
                text='狗狗'
            ),
            MessageTemplateAction(
                label='貓咪',
                text='貓咪'
            ),
        ]
        url = 'https://imgur.com/4DnqsWs.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_dog(self, event):
        global pet
        text = event.message.text

        if text == '狗狗':
            pet = '狗狗'
            return True
        return False

    def on_enter_dog(self, event):
        title = '想知道哪方面的資訊'
        text = '狗狗健康資訊'
        btn = [
            MessageTemplateAction(
                label='肥胖',
                text='肥胖'
            ),
            MessageTemplateAction(
                label='寄生蟲',
                text='寄生蟲'
            ),
            MessageTemplateAction(
                label='疾病',
                text='疾病'
            ),
            MessageTemplateAction(
                label='疫苗',
                text='疫苗'
            )
        ]
        url = 'https://imgur.com/Zj5KPKY.jpg'
        send_button_message(event.reply_token, title, text, btn, url)



    def is_going_to_cat(self, event):
        global pet
        text = event.message.text

        if text == '貓咪':
            pet = '貓咪'
            return True
        return False


    def on_enter_cat(self, event):
        title = '想知道哪方面的資訊'
        text = '貓咪健康資訊'
        btn = [
            MessageTemplateAction(
                label='肥胖',
                text='肥胖'
            ),
            MessageTemplateAction(
                label='寄生蟲',
                text='寄生蟲'
            ),MessageTemplateAction(
                label='疾病',
                text='疾病'
            ),
            MessageTemplateAction(
                label='疫苗',
                text='疫苗'
            )
        ]
        url = 'https://imgur.com/OkDNXIv.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    def is_going_to_dog_sick(self, event):
        text = event.message.text

        if text == '疾病':
            return True
        return False

    def on_enter_dog_sick(self, event):
        title = '四個常見的狗狗疾病'
        text = '狗狗和人類一樣,都有生病的機會,如何避免和治療就是相當重要的問題'
        btn = [
            MessageTemplateAction(
                label='心臟病',
                text='心臟病'
            ),
            MessageTemplateAction(
                label='傳染病',
                text='傳染病'
            ), MessageTemplateAction(
                label='惡性腫瘤',
                text='惡性腫瘤'
            ),
            MessageTemplateAction(
                label='腎臟病',
                text='腎臟病'
            )
        ]
        url = 'https://imgur.com/gPlgwTH.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    def is_going_to_dog_heart(self, event):
        text = event.message.text

        if text == '心臟病':
            return True
        return False

    def on_enter_dog_heart(self, event):
        text = '【症狀】：體溫提升、精神不佳、厭食、嘔吐、下痢、急性水樣出血性下痢 \n常見致死的重大惡性傳染病是犬瘟熱及犬小病毒腸炎，除了主人沒有確實施打預防針之外（預防針的施打率不到三分之一)，狗狗又無法自主管理生活環境，狗狗見面打招呼的方法確實比人類熱情多了，往往造成疾病傳染，所以最好的建議是定期施打預防針，並儘量避免被感染的機會，如果你家裡有新加入的狗狗成員，切記要先讓醫師做健康檢查並隔離一段時間做觀察。 \n【預防治療方式】：小心，別讓狗狗與其它來路不明的狗互相舔來舔去、定期施打預防針、抗血清治療並投以大量抗生素。'
        send_text_message(event.reply_token,text)
    def is_going_to_dog_infectious(self, event):
        text = event.message.text

        if text == '傳染病':
            return True
        return False
    def on_enter_dog_infectious(self, event):
        text = '【症狀】：容易喘、疲倦 \n基本上，狗狗心臟病的症狀跟人類很雷同，與肥胖、老化有關，但糟糕的是，主人常會因疏忽而延遲就醫導致狗狗死亡；還有很容易激動的犬種，常常因不知情的小朋友或親朋好友來訪時給予不當的過度運動，而發生急性休克的悲劇。 \n心臟病的診斷除了需要相當的經驗外，還要有必備的醫療檢驗設備來檢查，輔以長期的服藥、定期的追蹤及正確的飼養管理才能常保平安。 \n【預防治療方式】：避免狗狗肥胖、要適當運動、定期做Ｘ光、驗血、心電圖、杜普勒彩色心臟超音波檢查。'
        send_text_message(event.reply_token, text)
    def is_going_to_dog_cancer(self, event):
        text = event.message.text

        if text == '惡性腫瘤':
            return True
        return False
    def on_enter_dog_cancer(self, event):
        text = '【症狀】：很少有病徵 \n其實狗狗的惡性腫瘤，在獸醫師的臨床診療往往會被疏忽掉，尤其老年狗往往被直接認為只是老死。基本上，雖然狗狗在飲食上容易發胖，但不像人類有那麼多致癌食物，在日常生活上也不可能酗酒、熬夜，所以其發生的比例因此而降低。 \n要如何減少惡性腫瘤的發生？母狗節育可減少乳房瘤的發生、公狗節育可減少前列腺癌的發生、如果你發現你的狗狗得到隱睪症，應該儘早進行手術摘除，以避免間質細胞癌；狗狗處於室外時，要避免長期在陽光下曝曬，以避免上皮細胞癌，同時要避免肥胖及減少除蚤劑的使用，以免發生移形上皮細胞癌。 \n【預防治療方式】：定期做相關檢查。 '
        send_text_message(event.reply_token, text)
    def is_going_to_dog_kidney(self, event):
        text = event.message.text

        if text == '腎臟病':
            return True
        return False
    def on_enter_dog_kidney(self, event):
        text = '症狀】：出現血尿、排尿習慣改變或尿液顏色異常 \n狗狗腎臟問題的可怕性，主要是因為這腎臟病病程會不知不覺地感染，發覺腎臟出問題時，往往腎元細胞的損害已超過七十五％。 \n會發生腎臟疾病的原因，主要是狗狗的水攝取量不夠，而且主人為了自己的方便而減少狗排尿的次數，比如不喜歡狗狗在家裡隨地尿尿，又沒有空帶狗狗到戶外，而理所當然地以為狗狗一天只要尿一次到兩次，其實這樣是不夠的；加上許多主人常餵食狗狗人類的食物，使狗狗的腎臟因為鹽分負擔超過而受損；其它會引發腎臟疾病的原因還有尿路性的上行感染、泌尿系統結石的延遲發現，這都會對腎臟造成很大的損傷。\n【預防治療方式】：清淡飲食、排尿正常。 '
        send_text_message(event.reply_token, text)
    def is_going_to_dog_fat(self, event):
        text = event.message.text

        if text == '肥胖':
            return True
        return False
    def on_enter_dog_fat(self, event):

        title = '您家的狗狗的體型比較接近'
        text = '狗狗和人類一樣,如果過於的肥胖的話都會增加得到某些疾病的機率'
        btn = [
            MessageTemplateAction(
                label='過瘦',
                text='過瘦'
            ),
            MessageTemplateAction(
                label='適中',
                text='適中'
            ), MessageTemplateAction(
                label='過胖',
                text='過胖'
            ),
        ]
        url = 'https://imgur.com/Q4dIbsN.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_dog_too_fat(self, event):
        text = event.message.text

        if text == '過胖':
            return True
        return False

    def on_enter_dog_too_fat(self, event):
        text = '過胖的狗狗容易喘，走路跳躍時也會搖晃，從側邊來看有點像圓潤的香腸。\n請務必為過胖狗狗把關每日熱量攝取，以免體疾病找上身喔！\n ● 狗狗體重過重可能引發的疾病\n•關節炎\n•心血管疾病\n•糖尿病\n•呼吸疾病（例如：氣管塌陷）'
        send_text_message(event.reply_token , text)
    def is_going_to_dog_too_thin(self, event):
        text = event.message.text

        if text == '過瘦':
            return True
        return False

    def on_enter_dog_too_thin(self, event):
        text = '狗狗的肋骨、腰椎、骨盆清晰可見時，就屬於過瘦體型。此時全身最細的部位是腰部，且肚子缺乏脂肪。如果在野外遇到過瘦的狗狗，建議可以先為他們補充水份、再補充營養！'
        send_text_message(event.reply_token, text)
    def is_going_to_dog_median(self, event):
        text = event.message.text

        if text == '適中':
            return True
        return False

    def on_enter_dog_median(self, event):
        text = '若外觀沒有明顯的骨頭形狀，但是卻摸得到骨頭，腰部稍微內縮，屬於標準體型。通常標準體型的狗狗無明顯腰身，肚子稍有肉，用來保護內臟。狗狗若有適當運動，又沒有「過度飲食」的話，就能擁有完美體態！'
        send_text_message(event.reply_token, text)
    def is_going_to_dog_vaccine(self, event):
        text = event.message.text

        if text == '疫苗':
            return True
        return False

    def on_enter_dog_vaccine(self, event):
        url = 'https://imgur.com/vcgX4yN.jpg'
        send_image_message(event.reply_token, url)
    def is_going_to_dog_parasite(self, event):
        text = event.message.text

        if text == '寄生蟲':
            return True
        return False
    def on_enter_dog_parasite(self, event):
        url = 'https://imgur.com/MoberGh.jpg'
        send_image_message(event.reply_token, url)
    def is_going_to_cat_sick(self, event):
        text = event.message.text

        if text == '疾病':
            return True
        return False

    def on_enter_cat_sick(self, event):
        title = '四個常見的貓咪疾病'
        text = '貓咪和人類一樣,都有生病的機會,如何避免和治療就是相當重要的問題'
        btn = [
            MessageTemplateAction(
                label='慢性腎衰竭',
                text='慢性腎衰竭'
            ),
            MessageTemplateAction(
                label='肝炎',
                text='肝炎'
            ), MessageTemplateAction(
                label='糖尿病',
                text='糖尿病'
            ),
            MessageTemplateAction(
                label='牙科疾病',
                text='牙科疾病'
            )
        ]
        url = 'https://imgur.com/eNIYJqR.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_cat_kidney(self, event):
        text = event.message.text

        if text == '慢性腎衰竭':
            return True
        return False

    def on_enter_cat_kidney(self, event):
        text = '腎臟組織緩慢且持續性損壞，影響腎臟的正常功能，如代謝廢物排出、體內電解質平衡等，這種傷害是無法復原的。此為年老貓咪的最常見致死疾病，初期不易發現。可能的起因有很多，如尿石症、高血壓、偏酸性飲食、細茵感染發炎、遺傳、腫瘤等。\n徵兆  頻渴、多尿、食慾下降、虛弱、嘔吐、脫水、口腔潰瘍、下痢及貧血等。\n預防  除了讓貓咪多喝水之外，超過七歲老貓，每半年應定期做血液、尿液檢查、血壓測量等。由醫生觸診、X光檢查或超音波檢查也可即早發現。\n治療  輸液治療、定期服藥、改食用腎臟處方飼料、人工餵水、定期回診檢測腎臟功能等。'
        send_text_message(event.reply_token,text)
    def is_going_to_cat_liver(self, event):
        text = event.message.text

        if text == '肝炎':
            return True
        return False

    def on_enter_cat_liver(self, event):
        text = '肝炎指細菌由消化道入侵膽管而引起的感染。或由腫瘤、膽石造成膽管阻塞、甚至先天性缺陷也會促使肝炎發生。最終導致肝功能不正常，無法代謝體內毒素、產生黃疸等症狀。\n徵兆 有食慾但無法入食、沒精神、嗜睡、發燒、貧血、嘔吐黃水或泡沫、尿黃、內眼瞼或皮膚發黃等。\n預防  乾淨的衛生及良好的飲食習慣。定期血液檢查、施打疫苗、避免用藥過當。\n治療  藥物治療、飲食調理等。治療方式依疾病觸發的起因而不同。'
        send_text_message(event.reply_token,text)

    def is_going_to_cat_diabete(self, event):
        text = event.message.text

        if text == '糖尿病':
            return True
        return False

    def on_enter_cat_diabete(self, event):
        text = '糖尿病為胰腺生產的胰島素不足，或體內細胞無法吸收而導致的綜合病症。若沒有得到適當的控制，容易引起一些急性併發症。常見於十歲以上老貓或過胖貓咪，遺傳也是可能的起因。而公貓平均罹病比例大於母貓。\n徵兆  飲水量及尿量增加、食慾提升但體重卻下降、突然厭食等。\n預防  避免過胖、調整飲食計畫、增加貓咪運動量、定期檢查。\n治療  定時施打胰島素、改食用糖尿病處方飼料、定期回診進行尿糖及血糖的監測等。'
        send_text_message(event.reply_token, text)

    def is_going_to_cat_tooth(self, event):
        text = event.message.text

        if text == '牙科疾病':
            return True
        return False

    def on_enter_cat_tooth(self, event):
        text = '牙齒相關疾病有很多種，如蛀牙、牙齦炎、牙周病、口腔潰瘍。其中常發生的疾病為貓破牙細胞再吸收病害(Feline odontoclastic resorptive lesion, FORL)，由骨髓的破牙細胞造成齒質及牙根損壞，貓咪會感到受劇烈的疼痛，至病害末期時則導至牙齒脫落。\n徵兆  牙齒泛黃、有結石般附著物、牙齦泛紅腫脹或紅點、易流血、口臭、流口水、咀嚼困難、厭食等。\n預防  可供給潔牙式飼料、每日口腔牙齒清潔、定期洗牙、X光檢查。\n治療  藥物治療、洗牙、拔牙、牙冠截除、定期追蹤等。'
        send_text_message(event.reply_token, text)
    def is_going_to_cat_fat(self, event):
        text = event.message.text

        if text == '肥胖':
            return True
        return False
    def on_enter_cat_fat(self, event):

        title = '您家的貓咪的體型比較接近'
        text = '貓咪和人類一樣,如果過於的肥胖的話都會增加得到某些疾病的機率'
        btn = [
            MessageTemplateAction(
                label='過瘦',
                text='過瘦'
            ),
            MessageTemplateAction(
                label='適中',
                text='適中'
            ), MessageTemplateAction(
                label='過胖',
                text='過胖'
            ),
        ]
        url = 'https://imgur.com/bos21qx.jpg'
        send_button_message(event.reply_token, title, text, btn, url)


    def is_going_to_cat_too_fat(self, event):
        text = event.message.text

        if text == '過胖':
            return True
        return False

    def on_enter_cat_too_fat(self, event):
        text = '當貓咪脂肪過厚，用力搓揉也摸不太到骨頭，肚子有下垂的肉肉時，屬於過胖體型。\n通常過胖的貓咪走路跳躍時會搖晃，從上方看，體型像顆圓潤的瓠瓜。\n如果你的貓咪過胖了，請務必為他們每天攝取的熱量做把關，以免體重過重讓疾病找上身喔！\n如何知道如何檢查貓咪過胖貓咪太胖貓貓過瘦過胖體型體態體重超標太肥n● 喵喵體重過重可能引發的疾病\n•關節炎\n•心血管疾病\n•糖尿病\n•呼吸疾病（例如：氣管塌陷）'
        send_text_message(event.reply_token , text)
    def is_going_to_cat_too_thin(self, event):
        text = event.message.text

        if text == '過瘦':
            return True
        return False

    def on_enter_cat_too_thin(self, event):
        text = '當貓咪瘦得皮包骨，肋骨、腰椎、骨盆等都清晰可見時，就屬於過瘦體型。全身最細的部位是腰部，肚子也缺乏脂肪。通常無人餵養的流浪貓會呈現這種狀態，請趕緊為他們補充營養吧！'
        send_text_message(event.reply_token, text)
    def is_going_to_cat_median(self, event):
        text = event.message.text

        if text == '適中':
            return True
        return False

    def on_enter_cat_median(self, event):
        text = '骨頭「摸得到看不到」，外觀沒有明顯的骨頭形狀，腰部稍微內縮，屬於適中體型。這是標準的體態，無明顯腰身，但是肚子稍有肉肉，可以保護內臟。快看看家裡的貓主子是不是這種完美體態呢？'
        send_text_message(event.reply_token, text)
    def is_going_to_cat_vaccine(self, event):
        text = event.message.text

        if text == '疫苗':
            return True
        return False
    def on_enter_cat_vaccine(self, event):
        url = 'https://imgur.com/9ZpaqNY.jpg'
        send_image_message(event.reply_token, url)
    def is_going_to_cat_parasite(self, event):
        text = event.message.text

        if text == '寄生蟲':
            return True
        return False
    def on_enter_cat_parasite(self, event):
        url = 'https://imgur.com/HNacUf3.jpg'
        send_image_message(event.reply_token, url)
