from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from reservation.views import list_view

from . views import home_page,trek_in_nepal,peak_climbing_in_nepal, nepal_tour, rafting_in_nepal, jungle_safari_tour
from . views import volunteering_tour,adventure_sports,hotel_reservation,air_ticketing_in_nepal,mountain_expedition
from . views import sightseeing_tour, bird_watching_tour,day_tour,day_hiking_tour
from . views import trekking_info, everest_region, annapurna_region, langtang_region, restricted_area_trek, dolpo_region, ganesh_himal
from . views import trekking_season, trekking_types, trekking_grade
from . views import everest_base_camp_trek, jiri_everest_base_camp_trek, gokyo_renjo_la_pass_trek, gokyo_valley_trek, everest_view_trek, island_peak_climbing_everest
from . views import annapurna_base_camp_trek, ghorepani_poon_hill_trek, annapurna_sanctuary_trek, mardi_himal_trek, tilicho_lake_trek, annapurna_round_with_abc_trek, annapurna_view_trek, annapurna_circuit_biking_tour
from . views import langtang_gosaikunda_helambu_trek, langtang_gosaikunda_trek, tamang_heritage_treks, tamang_heritage_and_langtang_valley_trek
from . views import makalu_trek, manaslu_tea_house_trek, tsum_valley_trek, upper_dolpo_trek, upper_mustang_tea_house_trek, around_manaslu_trek
from . views import hindu_pilgrimage_tour, pokhara_city_tour, kathmandu_pokhara_sarangkot_tour, kathmandu_valley_trek, best_of_nepal_tour
from . views import pashupatinath, gosaikunda, devghat, muktinath_temple, damodarkunda, janakpur_ram_janaki_temple, ruru_riddi, manakamana, sworgadawari, barachchhetra, balmiki_ashram
from . views import island_peak_climbing, mera_peak_climbing, pisang_peak_climbing, tent_peak_climbing, yala_peak_climbing, paldor_peak_climbing, thorung_peak_climbing, singuchuli_peak_climbing
from . views import trisuli_river_rafting, kali_gandaki_river_rafting, karnali_river_rafting, sunkoshi_river_rafting, seti_river_rafting, bhotekoshi_river_rafting, dudh_koshi_rafting, tarun_river_rafting, marsyangdi_river_rafting, bheri_river_rafting, tamur_river_rafting
from . views import chitwan_jungle_safari_tour, bardia_jungle_safari_tour
from . views import paragliding_in_nepal, bungee_jumping_nepal, zip_flying, mountain_flights
from . views import everest_expedition, annapurna_expedition, manaslu_expedition, dhaulagiri_expedition, pumori_expedition, lhotse_expedition, amadablam_expedition, baruntse_expedition, cho_oyu_expedition
from . views import pokhara_valley_sightseeing, patan_durbar_square, pokhara_city_sightseeing
from . views import kathmandu_valley_bird_watching
from . views import shivapuri_hiking, nagarkot_hiking

from . views import about_page,contact_page,login_page

from . views import tours_in_india,bhutan,tours_in_bhutan,nepal

from . views import tours_in_tibet, trekking_in_tibet, tibet_mountain_expedition
from . views import kailash_tour, lhasa_tour, simikot_kailash_ebc_lhasa_tour


urlpatterns = [
    path('', home_page,name='home'),
    path('about/', about_page,name='about'),
    path('contact/', contact_page,name='contact'),
    path('login/', login_page,name='login'),

    path('nepal/trek-in-nepal/', trek_in_nepal,name='trek-in-nepal'),
    path('nepal/peak-climbing-in-nepal/', peak_climbing_in_nepal,name='peak-climbing-in-nepal'),
    path('nepal/nepal-tour/', nepal_tour,name='nepal-tour'),
    path('nepal/rafting-in-nepal/', rafting_in_nepal,name='rafting-in-nepal'),
    path('nepal/volunteering-tour/', volunteering_tour,name='volunteering-tour'),
    path('nepal/rafting-in-nepal/',rafting_in_nepal ,name='rafting-in-nepal'),
    path('nepal/jungle-safari-tour/', jungle_safari_tour,name='jungle-safari-tour'),
    path('nepal/air-ticketing-in-nepal/', air_ticketing_in_nepal,name='air-ticketing-in-nepal'),
    path('nepal/adventure-sports/',adventure_sports ,name='adventure-sports'),
    path('nepal/hotel-reservation/', hotel_reservation,name='hotel-reservation'),
    path('nepal/mountain-expedition/', mountain_expedition,name='mountain-expedition'),
    path('nepal/sightseeing-tour/', sightseeing_tour,name='sightseeing-tour'),
    path('nepal/bird-watching-tour/', bird_watching_tour,name='bird-watching-tour'),
    path('nepal/day-tour/', day_tour,name='day-tour'),
    path('nepal/day-hiking-tour/', day_hiking_tour,name='day-hiking-tour'),

    path('nepal/trek-in-nepal/trekking-info', trekking_info,name='trekking-info'),
    path('nepal/trek-in-nepal/everest-region', everest_region,name='everest-region'),
    path('nepal/trek-in-nepal/annapurna-region', annapurna_region,name='annapurna-region'),
    path('nepal/trek-in-nepal/langtang-region', langtang_region,name='langtang-region'),
    path('nepal/trek-in-nepal/restricted-area-trek', restricted_area_trek,name='restricted-area-trek'),
    path('nepal/trek-in-nepal/dolpo-region', dolpo_region,name='dolpo-region'),
    path('nepal/trek-in-nepal/ganesh-himal', ganesh_himal,name='ganesh-himal'),

    path('nepal/trek-in-nepal/trekking-info/trekking-season', trekking_season,name='trekking-season'),
    path('nepal/trek-in-nepal/trekking-info/trekking-types', trekking_types,name='trekking-types'),
    path('nepal/trek-in-nepal/trekking-info/trekking-grade', trekking_grade,name='trekking-grade'),

    path('nepal/trek-in-nepal/everest-region/everest-base-camp-trek', everest_base_camp_trek,name='everest-base-camp-trek'),
    path('nepal/trek-in-nepal/everest-region/jiri-everest-base-camp-trek', jiri_everest_base_camp_trek,name='jiri-everest-base-camp-trek'),
    path('nepal/trek-in-nepal/everest-region/gokyo-renjo-la-pass-trek', gokyo_renjo_la_pass_trek,name='gokyo-renjo-la-pass-trek'),
    path('nepal/trek-in-nepal/everest-region/gokyo-valley-trek', gokyo_valley_trek,name='gokyo-valley-trek'),
    path('nepal/trek-in-nepal/everest-region/everest-view-trek', everest_view_trek,name='everest-view-trek'),
    path('nepal/trek-in-nepal/everest-region/island-peak-climbing-everest', island_peak_climbing_everest,name='island-peak-climbing-everest'),

    path('nepal/trek-in-nepal/annapurna-region/annapurna-base-camp-trek', annapurna_base_camp_trek,name='annapurna-base-camp-trek'),
    path('nepal/trek-in-nepal/annapurna-region/ghorepani-poon-hill-trek', ghorepani_poon_hill_trek,name='ghorepani-poon-hill-trek'),
    path('nepal/trek-in-nepal/annapurna-region/annapurna-sanctuary-trek', annapurna_sanctuary_trek,name='annapurna-sanctuary-trek'),
    path('nepal/trek-in-nepal/annapurna-region/mardi-himal-trek', mardi_himal_trek,name='mardi-himal-trek'),
    path('nepal/trek-in-nepal/annapurna-region/tilicho-lake-trek', tilicho_lake_trek,name='tilicho-lake-trek'),
    path('nepal/trek-in-nepal/annapurna-region/annapurna-round-with-abc-trek', annapurna_round_with_abc_trek,name='annapurna-round-with-abc-trek'),
    path('nepal/trek-in-nepal/annapurna-region/annapurna-view-trek', annapurna_view_trek,name='annapurna-view-trek'),
    path('nepal/trek-in-nepal/annapurna-region/annapurna-circuit-biking-tour', annapurna_circuit_biking_tour,name='annapurna-circuit-biking-tour'),
   
    path('nepal/trek-in-nepal/langtang-region/langtang-gosainkunda-helambu-trek',langtang_gosaikunda_helambu_trek , name='langtang-gosaikunda-helambu-trek'),
    path('nepal/trek-in-nepal/langtang-region/langtang-gosainkunda-trek',langtang_gosaikunda_trek, name='langtang-gosaikunda-trek'),
    path('nepal/trek-in-nepal/langtang-region/tamang-heritage-treks',tamang_heritage_treks , name='tamang-heritage-treks'),
    path('nepal/trek-in-nepal/langtang-region/tamang-heritage-and-langtang-valley-trek',tamang_heritage_and_langtang_valley_trek, name='tamang-heritage-and-langtang-valley-trek'),

    path('nepal/trek-in-nepal/restricted-area-trek/makalu-trek', makalu_trek,name='makalu-trek'),
    path('nepal/trek-in-nepal/restricted-area-trek/manaslu-tea-house-trek', manaslu_tea_house_trek,name='manaslu-tea-house-trek'),
    path('nepal/trek-in-nepal/restricted-area-trek/tsum-valley-trek', tsum_valley_trek,name='tsum-valley-trek'),
    path('nepal/trek-in-nepal/restricted-area-trek/upper-dolpotrek', upper_dolpo_trek,name='upper-dolpo-trek'),
    path('nepal/trek-in-nepal/restricted-area-trek/upper-mustang-tea-house-trek', upper_mustang_tea_house_trek,name='upper-mustang-tea-house-trek'),
    path('nepal/trek-in-nepal/restricted-area-trek/around-manaslu-trek', around_manaslu_trek,name='around-manaslu-trek'),
    
    path('nepal/peak-climbing-in-nepal/island-peak-climbing', island_peak_climbing,name='island-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/mera-peak-climbing', mera_peak_climbing,name='mera-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/pisang-peak-climbing', pisang_peak_climbing,name='pisang-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/tent-peak-climbing', tent_peak_climbing,name='tent-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/yala-peak-climbing', yala_peak_climbing,name='yala-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/paldor-peak-climbing', paldor_peak_climbing,name='paldor-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/thorung-peak-climbing', thorung_peak_climbing,name='thorung-peak-climbing'),
    path('nepal/peak-climbing-in-nepal/singuchuli-peak-climbing', singuchuli_peak_climbing,name='singuchuli-peak-climbing'),

    path('nepal/nepal-tour/hindu-pilgrimage-tour',hindu_pilgrimage_tour ,name='hindu-pilgrimage-tour'),
    path('nepal/nepal-tour/pokhara-city-tour', pokhara_city_tour,name='pokhara-city-tour'),
    path('nepal/nepal-tour/kathmandu-pokhara-sarangkot-tour', kathmandu_pokhara_sarangkot_tour,name='kathmandu-pokhara-sarangkot-tour'),
    path('nepal/nepal-tour/kathmandu-valley-trek', kathmandu_valley_trek,name='kathmandu-valley-trek'),
    path('nepal/nepal-tour/best-of-nepal-tour', best_of_nepal_tour,name='best-of-nepal-tour'),

    path('nepal/nepal-tour/hindu-pilgrimage-tour/pashupatinath',pashupatinath ,name='pashupatinath'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/gosaikunda',gosaikunda ,name='gosaikunda'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/devghat',devghat ,name='devghat'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/muktinath-temple',muktinath_temple ,name='muktinath-temple'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/damodarkunda',damodarkunda ,name='damodarkunda'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/janakpur-ram-janaki-temple',janakpur_ram_janaki_temple ,name='janakpur-ram-janaki-temple'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/ruru-riddi',ruru_riddi ,name='ruru-riddi'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/manakamana',manakamana ,name='manakamana'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/sworgadawari',sworgadawari ,name='sworgadawari'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/barachchhetra',barachchhetra ,name='barachchhetra'),
    path('nepal/nepal-tour/hindu-pilgrimage-tour/balmiki-ashram',balmiki_ashram ,name='balmiki-ashram'),

    path('nepal/rafting-in-nepal/trisuli-river-rafting', trisuli_river_rafting,name='trisuli-river-rafting'),
    path('nepal/rafting-in-nepal/kali-gandaki-river-rafting', kali_gandaki_river_rafting,name='kali-gandaki-river-rafting'),
    path('nepal/rafting-in-nepal/karnali-river-rafting', karnali_river_rafting,name='karnali-river-rafting'),
    path('nepal/rafting-in-nepal/sunkoshi-river-rafting', sunkoshi_river_rafting,name='sunkoshi-river-rafting'),
    path('nepal/rafting-in-nepal/seti-river-rafting', seti_river_rafting,name='seti-river-rafting'),
    path('nepal/rafting-in-nepal/bhotekoshi-river-rafting', bhotekoshi_river_rafting,name='bhotekoshi-river-rafting'),
    path('nepal/rafting-in-nepal/dudh-koshi-rafting', dudh_koshi_rafting,name='dudh-koshi-rafting'),
    path('nepal/rafting-in-nepal/tarun-river-rafting', tarun_river_rafting,name='tarun-river-rafting'),
    path('nepal/rafting-in-nepal/marsyangdi-river-rafting', marsyangdi_river_rafting,name='marsyangdi-river-rafting'),
    path('nepal/rafting-in-nepal/bheri-river-rafting', bheri_river_rafting,name='bheri-river-rafting'),
    path('nepal/rafting-in-nepal/tamur-river-rafting', tamur_river_rafting,name='tamur-river-rafting'),

    path('nepal/jungle-safari-tour/chitwan-jungle-safari-tour', chitwan_jungle_safari_tour,name='chitwan-jungle-safari-tour'),
    path('nepal/jungle-safari-tour/bardia-jungle-safari-tour', bardia_jungle_safari_tour,name='bardia-jungle-safari-tour'),

    path('nepal/adventure-sports/paragliding-in-nepal',paragliding_in_nepal ,name='paragliding-in-nepal'),
    path('nepal/adventure-sports/bungee-jumping-nepal',bungee_jumping_nepal ,name='bungee-jumping-nepal'),
    path('nepal/adventure-sports/zip-flying',zip_flying ,name='zip-flying'),
    path('nepal/adventure-sports/mountain-flights',mountain_flights ,name='mountain-flights'),

    path('nepal/mountain-expedition/everest-expedition', everest_expedition,name='everest-expedition'),
    path('nepal/mountain-expedition/annapurna-expedition', annapurna_expedition,name='annapurna-expedition'),
    path('nepal/mountain-expedition/manaslu-expedition', manaslu_expedition,name='manaslu-expedition'),
    path('nepal/mountain-expedition/dhaulagiri-expedition', dhaulagiri_expedition,name='dhaulagiri-expedition'),
    path('nepal/mountain-expedition/pumori-expedition', pumori_expedition,name='pumori-expedition'),
    path('nepal/mountain-expedition/lhotse-expedition', lhotse_expedition,name='lhotse-expedition'),
    path('nepal/mountain-expedition/amadablam-expedition', amadablam_expedition,name='amadablam-expedition'),
    path('nepal/mountain-expedition/baruntse-expedition', baruntse_expedition,name='baruntse-expedition'),
    path('nepal/mountain-expedition/cho-oyu-expedition', cho_oyu_expedition,name='cho-oyu-expedition'),

    path('nepal/sightseeing-tour/pokhara-valley-sightseeing', pokhara_valley_sightseeing,name='pokhara-valley-sightseeing'),
    path('nepal/sightseeing-tour/patan-durbar-square', patan_durbar_square,name='patan-durbar-square'),
    path('nepal/sightseeing-tour/pokhara-city-sightseeing', pokhara_city_sightseeing,name='pokhara-city-sightseeing'),

    path('nepal/bird-watching-tour/kathmandu-valley-bird-watching', kathmandu_valley_bird_watching,name='kathmandu-valley-bird-watching'),

    path('nepal/day-hiking-tour/shivapuri-hiking', shivapuri_hiking,name='shivapuri-hiking'),
    path('nepal/day-hiking-tour/nagarkot-hiking', nagarkot_hiking,name='nagarkot-hiking'),
    
    path('bhutan',bhutan,name='bhutan'),
    path('nepal',nepal,name='nepal'),
    path('bhutan/tours-in-bhutan',tours_in_bhutan,name='tours-in-bhutan'),

    path('tibet/tours-in-tibet', tours_in_tibet,name='tours-in-tibet'),
    path('tibet/trekking-in-tibet', trekking_in_tibet,name='trekking-in-tibet'),
    path('tibet/tibet-mountain-expedition', tibet_mountain_expedition,name='tibet-mountain-expedition'),

    path('tibet/tours-in-tibet/kailash-tour', kailash_tour,name='kailash-tour'),
    path('tibet/tours-in-tibet/lhasa-tour', lhasa_tour,name='lhasa-tour'),
    path('tibet/tours-in-tibet/simikot-kailash-ebc-lhasa-tour', simikot_kailash_ebc_lhasa_tour,name='simikot-kailash-ebc-lhasa-tour'),
    path('india/tours-in-india', tours_in_india,name='tours-in-india'),

    

    path('admin/', admin.site.urls),
    path('admin/list', list_view, name='reservation_list' ),
    path('reservation/', include('reservation.urls')),
    path('hotel/', include('hotel.urls')),



]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
