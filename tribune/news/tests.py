from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        
        
        self.james=Editor(first_name='james',last_name='Muriuki',email='james@moringa.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing save method
    def test_save_method(self):
        self.james.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.james=Editor(first_name='james',last_name='Muriuki',email='jamesmuriuki@moringa.com')
        self.james.save_editor()

        #creating a new tg and saving it

        self.new_tag=tags(name='testing')
        self.new_tag.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all.delete()    
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news=Article.today_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)

