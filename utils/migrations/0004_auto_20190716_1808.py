# Generated by Django 2.2.3 on 2019-07-16 16:08

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_sitebranding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlinksrelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='footerlinksrelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='utils.FooterLinks'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, help_text='Your Facebook page URL', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.CharField(blank=True, help_text='Your Twitter username, without the @', max_length=255, null=True),
        ),
    ]
