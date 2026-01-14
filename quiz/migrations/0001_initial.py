import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='', max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Квиз',
                'verbose_name_plural': 'Квизы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Текст вопроса')),
                ('description', models.TextField(blank=True, default='', max_length=500, verbose_name='Описание')),
                ('options', models.JSONField(verbose_name='Варианты ответа')),
                ('correct_answer', models.CharField(max_length=500, verbose_name='Правильный ответ')),
                ('explanation', models.TextField(blank=True, default='', max_length=250, verbose_name='Пояснение')),
                (
                    'difficulty',
                    models.CharField(
                        choices=[
                            ('easy', 'Лёгкий'),
                            ('medium', 'Средний'),
                            ('hard', 'Сложный'),
                        ],
                        default='easy',
                        max_length=6,
                        verbose_name='Сложность',
                    ),
                ),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='questions',
                        to='quiz.category',
                        verbose_name='Категория',
                    ),
                ),
                (
                    'quiz',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='questions',
                        to='quiz.quiz',
                        verbose_name='Квиз',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
