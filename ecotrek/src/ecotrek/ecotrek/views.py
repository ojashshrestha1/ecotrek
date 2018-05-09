from django.contrib.auth import authenticate, login,get_user_model

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  LoginForm 
from hotel.models import Hotel


def login_page(request):
	form = LoginForm(request.POST or None)
	context={
		"form":form
	}
	
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		print(user)
		
		if user is not None:
			login(request, user)
			return redirect("/admin")
		else:			
			print("Error")

	return render(request, "auth/login.html", context)


# Create your views here.
def home_page(request):
	return render(request,'home_page.html',{})

def about_page(request):
	return render(request,'about_page.html',{})

def contact_page(request):
	return render(request,'contact_page.html',{})

#Nepal sub pages
def trek_in_nepal(request):
	return render(request,'html/trek-in-nepal.html',{})

def peak_climbing_in_nepal(request):
	return render(request,'html/peak-climbing-in-nepal.html',{})

def nepal_tour(request):
	return render(request,'html/nepal-tour.html',{})

def rafting_in_nepal(request):
	return render(request,'html/rafting-in-nepal.html',{})

def jungle_safari_tour(request):
	return render(request,'html/jungle-safari-tour.html',{})

def volunteering_tour(request):
	return render(request,'html/volunteering-tour.html',{})

def adventure_sports(request):
	return render(request,'html/adventure-sports.html',{})

def hotel_reservation(request):
	qs=Hotel.objects.all()
	context={
		'obj_list':qs,
	}
	return render(request,'html/hotel-reservation.html',context)

def air_ticketing_in_nepal(request):
	return render(request,'html/air-ticketing.html',{})

def mountain_expedition(request):
	return render(request,'html/mountain-expedition.html',{})

def sightseeing_tour(request):
	return render(request,'html/sightseeing-tour.html',{})

def bird_watching_tour(request):
	return render(request,'html/bird-watching-tour.html',{})

def day_tour(request):
	return render(request,'html/day-tour.html',{})

def day_hiking_tour(request):
	return render(request,'html/day-hiking-tour.html',{})
#Nepal sub pages

# Trek in Nepal sub pages
def trekking_info(request):
	return render(request,'html/trekking-info.html',{})

def everest_region(request):
	return render(request,'html/everest-region.html',{})

def annapurna_region(request):
	return render(request,'html/annapurna-region.html',{})

def langtang_region(request):
	return render(request,'html/langtang-region.html',{})

def restricted_area_trek(request):
	return render(request,'html/restricted-area-trek.html',{})

def dolpo_region(request):
	return render(request,'html/dolpo-region.html',{})

def ganesh_himal(request):
	return render(request,'html/ganesh-himal.html',{})
# Trek in Nepal sub pages

# Trekking info sub pages
def trekking_season(request):
	return render(request,'html/trekking-season.html',{})

def trekking_types(request):
	return render(request,'html/trekking-types.html',{})

def trekking_grade(request):
	return render(request,'html/trekking-grade.html',{})

# Everest Region sub pages
def everest_base_camp_trek(request):
	return render(request,'html/everest-base-camp-trek.html',{})

def jiri_everest_base_camp_trek(request):
	return render(request,'html/jiri-everest-base-camp-trek.html',{})

def gokyo_renjo_la_pass_trek(request):
	return render(request,'html/gokyo-renjo-la-pass-trek.html',{})

def gokyo_valley_trek(request):
	return render(request,'html/gokyo-valley-trek.html',{})

def everest_view_trek(request):
	return render(request,'html/everest-view-trek.html',{})

def island_peak_climbing_everest(request):
	return render(request,'html/island-peak-climbing-everest.html',{})
# Everest Region sub pages

#Annapurna region sub pages
def annapurna_base_camp_trek(request):
	return render(request,'html/annapurna-base-camp-trek.html',{})

def ghorepani_poon_hill_trek(request):
	return render(request,'html/ghorepani-poon-hill-trek.html',{})

def annapurna_sanctuary_trek(request):
	return render(request, 'html/annapurna-sanctuary-trek.html', {})

def mardi_himal_trek(request):
	return render(request, 'html/mardi-himal-trek.html', {})

def tilicho_lake_trek(request):
	return render(request, 'html/tilicho-lake-trek.html', {})

def annapurna_round_with_abc_trek(request):
	return render(request, 'html/annapurna-round-with-abc-trek.html', {})

def annapurna_view_trek(request):
	return render(request, 'html/annapurna-view-trek.html', {})

def annapurna_circuit_biking_tour(request):
	return render(request, 'html/annapurna-circuit-biking-tour.html', {})
#Annapurna region sub pages

#Langtang region sub pages
def langtang_gosaikunda_helambu_trek(request):
	return render(request,'html/langtang-gosaikunda-helambu-trek.html',{})

def langtang_gosaikunda_trek(request):
	return render(request,'html/langtang-gosaikunda-trek.html',{})

def tamang_heritage_treks(request):
	return render(request,'html/tamang-heritage-treks.html',{})

def tamang_heritage_and_langtang_valley_trek(request):
	return render(request,'html/tamang-heritage-and-langtang-valley-trek.html',{})
#Langtang region sub pages

#Restricted Area Sub pages
def makalu_trek(request):
	return render(request,'html/makalu-trek.html',{})

def manaslu_tea_house_trek(request):
	return render(request,'html/manaslu-tea-house-trek.html',{})

def tsum_valley_trek(request):
	return render(request,'html/tsum-valley-trek.html',{})

def upper_dolpo_trek(request):
	return render(request,'html/upper-dolpo-trek.html',{})

def upper_mustang_tea_house_trek(request):
	return render(request,'html/upper-mustang-tea-house-trek.html',{})

def around_manaslu_trek(request):
	return render(request,'html/around-manaslu-trek.html',{})
#Restricted Area Sub pages

#Peak Climbing in Nepal sub pages
def island_peak_climbing(request):
	return render(request,'html/island-peak-climbing.html',{})

def mera_peak_climbing(request):
	return render(request,'html/mera-peak-climbing.html',{})

def pisang_peak_climbing(request):
	return render(request,'html/pisang-peak-climbing.html',{})

def tent_peak_climbing(request):
	return render(request,'html/tent-peak-climbing.html',{})

def yala_peak_climbing(request):
	return render(request,'html/yala-peak-climbing.html',{})

def paldor_peak_climbing(request):
	return render(request,'html/paldor-peak-climbing.html',{})

def thorung_peak_climbing(request):
	return render(request,'html/thorung-peak-climbing.html',{})

def singuchuli_peak_climbing(request):
	return render(request,'html/singuchuli-peak-climbing.html',{})
#Peak Climbing in Nepal sub pages

#nepal tour sub pages
def hindu_pilgrimage_tour(request):
	return render(request,'html/hindu-pilgrimage-tour.html',{})

def pokhara_city_tour(request):
	return render(request,'html/pokhara-city-tour.html',{})

def kathmandu_pokhara_sarangkot_tour(request):
	return render(request,'html/kathmandu-pokhara-sarangkot-tour.html',{})

def kathmandu_valley_trek(request):
	return render(request,'html/kathmandu-valley-trek.html',{})

def best_of_nepal_tour(request):
	return render(request,'html/best-of-nepal-tour.html',{})
#nepal tour sub pages

#hindu pilgrimage sub pages
def pashupatinath(request):
	return render(request,'html/pashupatinath.html',{})

def gosaikunda(request):
	return render(request,'html/gosaikunda.html',{})

def devghat(request):
	return render(request,'html/devghat.html',{})

def muktinath_temple(request):
	return render(request,'html/muktinath-temple.html',{})

def damodarkunda(request):
	return render(request,'html/damodarkunda.html',{})

def janakpur_ram_janaki_temple(request):
	return render(request,'html/janakpur-ram-janaki-temple.html',{})

def ruru_riddi(request):
	return render(request,'html/ruru-riddi.html',{})

def manakamana(request):
	return render(request,'html/manakamana.html',{})

def sworgadawari(request):
	return render(request,'html/sworgadawari.html',{})

def barachchhetra(request):
	return render(request,'html/barachchhetra.html',{})

def balmiki_ashram(request):
	return render(request,'html/balmiki-ashram.html',{})
#hindu pilgrimage sub pages

#Rafting in Nepal subpages
def trisuli_river_rafting(request):
	return render(request,'html/trisuli-river-rafting.html',{})

def kali_gandaki_river_rafting(request):
	return render(request,'html/kali-gandaki-river-rafting.html',{})

def karnali_river_rafting(request):
	return render(request,'html/karnali-river-rafting.html',{})

def sunkoshi_river_rafting(request):
	return render(request,'html/sunkoshi-river-rafting.html',{})

def seti_river_rafting(request):
	return render(request,'html/seti-river-rafting.html',{})

def bhotekoshi_river_rafting(request):
	return render(request,'html/bhotekoshi-river-rafting.html',{})

def dudh_koshi_rafting(request):
	return render(request,'html/dudh-koshi-rafting.html',{})

def tarun_river_rafting(request):
	return render(request,'html/tarun-river-rafting.html',{})

def marsyangdi_river_rafting(request):
	return render(request,'html/marsyangdi-river-rafting.html',{})

def bheri_river_rafting(request):
	return render(request,'html/bheri-river-rafting.html',{})

def tamur_river_rafting(request):
	return render(request,'html/tamur-river-rafting.html',{})
#Rafting in Nepal subpages

#Jungle safari Tour sub pages
def chitwan_jungle_safari_tour(request):
	return render(request,'html/chitwan-jungle-safari-tour.html',{})

def bardia_jungle_safari_tour(request):
	return render(request,'html/bardia-jungle-safari-tour.html',{})
#Jungle safari Tour sub pages

#Adventure Sports sub pages
def paragliding_in_nepal(request):
	return render(request,'html/paragliding-in-nepal.html',{})

def bungee_jumping_nepal(request):
	return render(request,'html/bungee-jumping-nepal.html',{})

def zip_flying(request):
	return render(request,'html/zip-flying.html',{})

def mountain_flights(request):
	return render(request,'html/mountain-flights.html',{})
#Adventure Sports sub pages

#Mountain Expedition sub pages
def everest_expedition(request):
	return render(request,'html/everest-expedition.html',{})

def annapurna_expedition(request):
	return render(request,'html/annapurna-expedition.html',{})

def manaslu_expedition(request):
	return render(request,'html/manaslu-expedition.html',{})

def dhaulagiri_expedition(request):
	return render(request,'html/dhaulagiri-expedition.html',{})

def pumori_expedition(request):
	return render(request,'html/pumori-expedition.html',{})

def lhotse_expedition(request):
	return render(request,'html/lhotse-expedition.html',{})

def amadablam_expedition(request):
	return render(request,'html/amadablam-expedition.html',{})

def baruntse_expedition(request):
	return render(request,'html/baruntse-expedition.html',{})

def cho_oyu_expedition(request):
	return render(request,'html/cho-oyu-expedition.html',{})
#Mountain Expedition sub pages

#Sightseeing sub pages
def pokhara_valley_sightseeing(request):
	return render(request,'html/pokhara-valley-sightseeing.html',{})

def patan_durbar_square(request):
	return render(request,'html/patan-durbar-square.html',{})

def pokhara_city_sightseeing(request):
	return render(request,'html/pokhara-city-sightseeing.html',{})
#Sightseeing sub pages

#bird watching tour sub page
def kathmandu_valley_bird_watching(request):
	return render(request,'html/kathmandu-valley-bird-watching.html',{})
#bird watching tour sub page

#day hiking tour sub pages
def shivapuri_hiking(request):
	return render(request,'html/shivapuri-hiking.html',{})

def nagarkot_hiking(request):
	return render(request,'html/nagarkot-hiking.html',{})
#day hiking tour sub pages

def nepal(request):
	return render(request,'html/nepal.html',{})

def bhutan(request):
	return render(request,'html/bhutan.html',{})

def tours_in_bhutan(request):
	return render(request,'html/tours-in-bhutan.html',{})

# Tibet sub pages
def tours_in_tibet(request):
	return render(request,'html/tours-in-tibet.html',{})

def trekking_in_tibet(request):
	return render(request,'html/trekking-in-tibet.html',{})

def tibet_mountain_expedition(request):
	return render(request,'html/tibet-mountain-expedition.html',{})
# Tibet sub pages

# tours in tibet sub pages
def kailash_tour(request):
	return render(request,'html/kailash-tour.html',{})

def lhasa_tour(request):
	return render(request,'html/lhasa-tour.html',{})

def simikot_kailash_ebc_lhasa_tour(request):
	return render(request,'html/simikot-kailash-ebc-lhasa-tour.html',{})
# tours in tibet sub pages

def tours_in_india(request):
	return render(request,'html/tours-in-india.html',{})




