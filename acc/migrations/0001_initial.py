# Generated by Django 4.0.1 on 2022-01-29 08:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='??????????')),
                ('is_email_verify', models.BooleanField(default=False)),
                ('is_sick', models.BooleanField(blank=True, default=False)),
                ('is_doctor', models.BooleanField(blank=True, default=False)),
                ('is_secretary', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='??????')),
                ('last_name', models.CharField(max_length=255, verbose_name='?????? ????????????????')),
                ('address_office', models.TextField(verbose_name='???????? ??????')),
                ('telphone_number_office', models.CharField(max_length=11, verbose_name='???????? ??????')),
                ('image_profile', models.ImageField(blank=True, upload_to='image profile doctor', verbose_name='?????? ??????????????')),
                ('is_doctor', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='??????')),
                ('last_name', models.CharField(max_length=255, verbose_name='?????? ????????????????')),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='???? ??????')),
                ('birth_certificate_code', models.CharField(max_length=10, unique=True, verbose_name='?????????? ????????????????')),
                ('father_name', models.CharField(max_length=255, verbose_name='?????? ??????')),
                ('province_of_residence', models.CharField(choices=[('azarbayejan_sh', '?????????????????? ????????'), ('azarbayejan_qh', '?????????????????? ????????'), ('ardabil', '????????????'), ('esfehan', '????????????'), ('alborz', '??????????'), ('elam', '??????????'), ('bohsher', '??????????'), ('tehran', '??????????'), ('charmahalbakhtiary', '???????? ???????? ?? ??????????????'), ('khorasan_j', '?????????? ??????????'), ('khorasan_r', '???????????? ????????'), ('khorasan_sh', '???????????? ??????????'), ('khozestan', '??????????????'), ('zanjan', '??????????'), ('semnan', '??????????'), ('sistanbalochestan', '???????????? ?? ????????????????'), ('fars', '????????'), ('qhazvin', '??????????'), ('qhom', '????'), ('kordestan', '??????????????'), ('kerman', '??????????'), ('kermanshah', '????????????????'), ('kohgiloboerahmad', '???????????????? ?? ????????????????'), ('golestan', '????????????'), ('gilan', '??????????'), ('lorestan', '????????????'), ('mazandaran', '????????????????'), ('markazi', '??????????'), ('hormozgan', '??????????????'), ('hamedan', '??????????'), ('yazd', '??????')], max_length=18, verbose_name='?????????? ?????? ??????????')),
                ('phone_number', models.CharField(max_length=11, verbose_name='?????????? ????????????')),
                ('image_profile', models.ImageField(blank=True, upload_to='image profile sick', verbose_name='?????? ??????????????')),
                ('is_sick', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='??????????')),
            ],
        ),
    ]
