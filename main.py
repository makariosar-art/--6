from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

# Настройка цвета фона приложения (темно-синий ctOS)
Window.clearcolor = get_color_from_hex('#050b14')

class CtOSMobileApp(App):
    def build(self):
        # Главный контейнер (вертикальный)
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # 1. ШАПКА ИНТЕРФЕЙСА
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
        title = Label(
            text="ctOS // MOBILE_V2.0 (PYTHON)",
            font_size='20sp',
            bold=True,
            color=get_color_from_hex('#00ffcc'),
            halign='center'
        )
        status = Label(
            text="ПОДКЛЮЧЕНИЕ К СЕТИ УСТАНОВЛЕНО",
            font_size='12sp',
            color=get_color_from_hex('#ff3366'),
            halign='center'
        )
        header.add_widget(title)
        header.add_widget(status)
        main_layout.add_widget(header)

        # 2. ТЕРМИНАЛ ЛОГОВ (Скроллинг)
        self.scroll_view = ScrollView(size_hint=(1, 0.5))
        self.terminal = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.terminal.bind(minimum_height=self.terminal.setter('height'))
        
        self.scroll_view.add_widget(self.terminal)
        main_layout.add_widget(self.scroll_view)

        # Стартовые логи
        self.add_log("Инициализация протокола DedSec...", '#00ffcc')
        self.add_log("Python-движок готов к работе на смартфоне.", '#00ffcc')

        # 3. ПАНЕЛЬ КНОПОК (Сетка 2х2 для удобного нажатия пальцами)
        controls = GridLayout(cols=2, spacing=10, size_hint_y=0.4)

        # Кнопки взлома
        btn_traffic = Button(text="СВЕТОФОРЫ", background_color=get_color_from_hex('#0a1626'), color=get_color_from_hex('#00ffcc'))
        btn_traffic.bind(on_press=lambda x: self.trigger_hack('traffic'))

        btn_bank = Button(text="СЧЕТ ГРАЖДАНИНА", background_color=get_color_from_hex('#0a1626'), color=get_color_from_hex('#00ffcc'))
        btn_bank.bind(on_press=lambda x: self.trigger_hack('bank'))

        btn_camera = Button(text="КАМЕРА УЛИЧНАЯ", background_color=get_color_from_hex('#0a1626'), color=get_color_from_hex('#00ffcc'))
        btn_camera.bind(on_press=lambda x: self.trigger_hack('camera'))

        btn_blackout = Button(text="БЛЭКАУТ", background_color=get_color_from_hex('#260a16'), color=get_color_from_hex('#ff3366'))
        btn_blackout.bind(on_press=lambda x: self.trigger_hack('blackout'))

        controls.add_widget(btn_traffic)
        controls.add_widget(btn_bank)
        controls.add_widget(btn_camera)
        controls.add_widget(btn_blackout)
        
        main_layout.add_widget(controls)

        # База данных фраз взлома
        self.phrases = {
            'traffic': ("[ВЗЛОМ] Переключение светофоров на перекрестке...", "[УСПЕХ] Создана аварийная ситуация. Погоня оторвалась."),
            'bank': ("[ВЗЛОМ] Сканирование NFC кошельков прохожих...", "[УСПЕХ] Переведено $450 на счет DedSec."),
            'camera': ("[ВЗЛОМ] Подключение к камере ctOS...", "[УСПЕХ] Трансляция выведена на экран. Скрытность +100%."),
            'blackout': ("[КРИТИЧЕСКИЙ ВЗЛОМ] Перегрузка подстанции...", "[ВНИМАНИЕ] Район погружен во тьму! Все системы отключены.")
        }

        return main_layout

    def add_log(self, text, color_hex):
        """Добавляет строку в терминал"""
        log_label = Label(
            text=f"> {text}",
            font_size='14sp',
            color=get_color_from_hex(color_hex),
            size_hint_y=None,
            height=30,
            halign='left',
            valign='middle'
        )
        log_label.bind(size=log_label.setter('text_size'))
        self.terminal.add_widget(log_label)
        # Автоматическая прокрутка вниз
        Clock.schedule_once(lambda dt: setattr(self.scroll_view, 'scroll_y', 0))

    def trigger_hack(self, hack_type):
        start_msg, success_msg = self.phrases[hack_type]
        color = '#ff3366' if hack_type == 'blackout' else '#ffcc00'
        
        # Выводим первое сообщение о начале взлома
        self.add_log(start_msg, color)
        
        # Симулируем задержку взлома в 1 секунду перед успехом
        success_color = '#ff3366' if hack_type == 'blackout' else '#00ffcc'
        Clock.schedule_once(lambda dt: self.add_log(success_msg, success_color), 1)

if __name__ == '__main__':
    CtOSMobileApp().run()
      kivy.appkivy.uix.boxlayoutkivy.uix.gridlayoutkivy.uix.buttonkivy.uix.scrollviewkivy.uix.labelkivy.core.windowkivy.clockkivy.utilsWindow.clearcolorself.terminalself.phrases1
