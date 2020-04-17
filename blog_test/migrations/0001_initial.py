# Generated by Django 3.0.2 on 2020-04-16 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('author', models.CharField(max_length=16, verbose_name='作者')),
                ('content', models.TextField(verbose_name='博客正文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.CharField(max_length=240, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_test.Blog', verbose_name='博客')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_test.Catagory', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog_test.Tag', verbose_name='标签'),
        ),
    ]