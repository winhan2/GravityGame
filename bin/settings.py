# coding: utf-8


class Settings(object):
    def __init__(self, sub_window, entrys, lang_dic, config):
        self.entrys = entrys
        self.sub_window = sub_window
        self.LANG_DIC = lang_dic
        self.config = config

    def save(self):
        # if not os.path.isfile(self.entrys[0].get()):
        #     messagebox.showerror(self.LANG_DIC['error'], f'keys_save_path_entry: {self.LANG_DIC["nip"]}')
        #     return
        # elif not self.entrys[1].get().isdigit():
        #     messagebox.showerror(self.LANG_DIC['error'], f'default_key_len_entry: {self.LANG_DIC["ndi"]}')
        #     return
        # elif not os.path.isdir(self.entrys[2].get()):
        #     messagebox.showerror(self.LANG_DIC['error'], f'e_path_entry: {self.LANG_DIC["nip"]}')
        #     return
        # elif not os.path.isdir(self.entrys[3].get()):
        #     messagebox.showerror(self.LANG_DIC['error'], f'd_path_entry: {self.LANG_DIC["nip"]}')
        #     return
        # elif not os.path.isdir(self.entrys[4].get()):
        #     messagebox.showerror(self.LANG_DIC['error'], f'e_default_dir_entry: {self.LANG_DIC["nip"]}')
        #     return
        # elif not os.path.isdir(self.entrys[5].get()):
        #     messagebox.showerror(self.LANG_DIC['error'], f'd_default_dir_entry: {self.LANG_DIC["nip"]}')
        #     return

        self.config.set('keys', 'save_path', self.entrys[0].get())
        self.config.set('keys', 'default_key_len', self.entrys[1].get())
        self.config.set('e_d_file', 'e_path', self.entrys[2].get())
        self.config.set('e_d_file', 'd_path', self.entrys[3].get())
        self.config.set('e_d_file', 'e_default_dir', self.entrys[4].get())
        self.config.set('e_d_file', 'd_default_dir', self.entrys[5].get())