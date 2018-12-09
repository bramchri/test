import os

from django.core.management.base import BaseCommand

from storage.models import Dictionary
from django.core.exceptions import MultipleObjectsReturned

FILENAME = 'words_dictionary.txt'


class Command(BaseCommand):
    help = 'Update model Dictionary'

    def handle(self, *args, **options):

        print('\nStarting dictionary update...')
        self.create_or_update_words_to_dictionary()
        print('Dictionary successfully updated')

    def create_or_update_words_to_dictionary(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        fullpath = os.path.join(dir_path, FILENAME)
        count = {'bad':0, 'good':0}

        with open(fullpath) as file:
            for line in file:
                word = line.strip()
                try:
                    if len(word)<2 or len(word)>125:
                        message = 'Word should contain more than 2 and less than 125 symbols: {}'.format(word)
                        count['bad']+=1
                        self.stdout.write(self.style.WARNING(message))
                        continue
                    obj, created = Dictionary.objects.update_or_create(name=word, defaults={'name': word})
                except MultipleObjectsReturned:
                    message = 'Exception: {}'.format(word)
                    self.stdout.write(self.style.WARNING(message))
                if created:
                    count['good'] += 1
                    message = 'Added a new word to the dictionary: {}'.format(word)
                    self.stdout.write(self.style.SUCCESS(message))
                else:
                    count['bad'] += 1
                    message = 'This word is already in the dictionary: {}'.format(word)
                    self.stdout.write(self.style.ERROR(message))
            self.stdout.write(self.style.ERROR('GOOD'+ str(count['good'])))
            self.stdout.write(self.style.ERROR('BAD' + str(count['bad'])))
