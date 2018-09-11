'''
    Copyright (C) 2017 Gitcoin Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Token, KudosTransfer, Wallet


class GeneralAdmin(admin.ModelAdmin):
    ordering = ['-id']


class TokenAdmin(admin.ModelAdmin):
    ordering = ['-id']


# class WalletAdmin(admin.ModelAdmin):
#     ordering = ['-id']


admin.site.register(Token, TokenAdmin)
admin.site.register(KudosTransfer, GeneralAdmin)
admin.site.register(Wallet, GeneralAdmin)
# admin.site.register(Wallet, WalletAdmin)
