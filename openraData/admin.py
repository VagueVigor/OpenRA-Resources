from django.contrib import admin

from openraData.models import Maps
from openraData.models import Units
from openraData.models import Mods
from openraData.models import Palettes
from openraData.models import Replays
from openraData.models import CrashReports
from openraData.models import Comments
from openraData.models import Screenshots
from openraData.models import Reports
from openraData.models import UserOptions

admin.site.register(Maps)
admin.site.register(Units)
admin.site.register(Mods)
admin.site.register(Palettes)
admin.site.register(Replays)
admin.site.register(CrashReports)
admin.site.register(Comments)
admin.site.register(Screenshots)
admin.site.register(Reports)
admin.site.register(UserOptions)
