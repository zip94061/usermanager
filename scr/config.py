import json
import logging

from pathlib import Path

class Config:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config_file = Path('config', 'config.json')
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.config_data = {
            'database': None,
            'emails': [],
            'domains': []
                            }

        if not self.config_file.exists():
            self.export_to_config_file()
        else:
            self.config_data = self.import_from_config_file()

    @property
    def database_path(self):
        return self.config_data['database']

    @database_path.setter
    def database_path(self, path):
        self.config_data['database'] = path
        self.export_to_config_file()

    @property
    def emails(self):
       return self.config_data['emails']

    @emails.setter
    def emails(self,email):
        self.config_data['emails'].apppend(email)

    @property
    def domains(self):
        return self.config_data['domains']

    @domains.setter
    def domains(self, domain):
        self.config_data['domains'].append(domain)

    def export_to_config_file(self):
        with open(self.config_file, 'w', encoding='utf-8') as file:
            json.dump(self.config_data, file, ensure_ascii=False, indent=4)
            self.logger.info('config.json обновлен')

    def import_from_config_file(self):
        with open(self.config_file, 'r', encoding='utf-8') as file:
            self.logger.info('config.json загружен')
            return json.load(file)
