#
# -*- coding: utf-8 -*- vim:fileencoding=utf-8:
# Copyright © 2014 Greek Research and Technology Network (GRNET S.A.)
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.

from django.contrib.auth import logout

class ForceLogoutMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated() and request.user.get_profile().force_logout_date and \
           ( 'LAST_LOGIN_DATE' not in request.session or \
             request.session['LAST_LOGIN_DATE'] < request.user.get_profile().force_logout_date ):
            logout(request)