# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from sorl.thumbnail import get_thumbnail
from project.travel.models import Country, Post, PostPhoto
from project.lists.models import Entry


class Command(BaseCommand):
    help = 'Pre-generate all sorl-thumbnail thumbnails used across the site'

    def handle(self, *args, **options):
        total = 0

        # Posts: headImage and titleImage
        self.stdout.write('Generating post thumbnails...')
        posts = Post.objects.filter(draft=False).exclude(headImage='').exclude(titleImage='')
        for post in posts:
            specs = []
            if post.headImage:
                specs += [
                    (post.headImage, 'x400', {'crop': 'left'}),
                    (post.headImage, 'x400', {'crop': 'center'}),
                ]
            if post.titleImage:
                specs += [
                    (post.titleImage, 'x400', {}),
                    (post.titleImage, '500x300', {}),
                ]
            for field, size, opts in specs:
                try:
                    get_thumbnail(field, size, **opts)
                    total += 1
                except Exception as e:
                    self.stderr.write(f'  Post {post.id} {size}: {e}')
        self.stdout.write(f'  {posts.count()} posts done.')

        # PostPhotos: photo and photoRight
        self.stdout.write('Generating post photo thumbnails...')
        photos = PostPhoto.objects.select_related('post').filter(post__draft=False)
        for pp in photos:
            for field in [pp.photo, pp.photoRight]:
                if not field:
                    continue
                for size in ['x1200', 'x400', 'x333']:
                    try:
                        get_thumbnail(field, size)
                        total += 1
                    except Exception as e:
                        self.stderr.write(f'  PostPhoto {pp.id} {size}: {e}')
        self.stdout.write(f'  {photos.count()} photo blocks done.')

        # Countries: ball and flag
        self.stdout.write('Generating country thumbnails...')
        countries = Country.objects.all()
        for country in countries:
            if country.ball:
                for size, opts in [('x73', {'format': 'PNG'}), ('x150', {'format': 'PNG'})]:
                    try:
                        get_thumbnail(country.ball, size, **opts)
                        total += 1
                    except Exception as e:
                        self.stderr.write(f'  Country {country.slug} ball {size}: {e}')
            if country.flag:
                try:
                    get_thumbnail(country.flag, '75')
                    total += 1
                except Exception as e:
                    self.stderr.write(f'  Country {country.slug} flag: {e}')
        self.stdout.write(f'  {countries.count()} countries done.')

        # List entries: itemImage
        self.stdout.write('Generating list entry thumbnails...')
        entries = Entry.objects.filter(published=True).exclude(itemImage=None).exclude(itemImage='')
        for entry in entries:
            try:
                get_thumbnail(entry.itemImage, 'x400')
                total += 1
            except Exception as e:
                self.stderr.write(f'  Entry {entry.id}: {e}')
        self.stdout.write(f'  {entries.count()} entries done.')

        self.stdout.write(self.style.SUCCESS(f'Done. {total} thumbnails generated.'))
