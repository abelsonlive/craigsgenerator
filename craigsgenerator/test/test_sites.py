import os

from nose.tools import assert_set_equal

from craigsgenerator.sites import sites

def test_sites():
    def fake_get():
        raise AssertionError('This should not be run.')
    d = os.path.join('craigsgenerator','test','fixtures','sites')
    observed = sites(get = fake_get, cachedir = d)
    expected = {'cosprings.craigslist.org', 'virgin.craigslist.org', 'albanyga.craigslist.org', 'cebu.craigslist.com.ph', 'zamboanga.craigslist.com.ph', 'xian.craigslist.com.cn', 'hiltonhead.craigslist.org', 'mazatlan.craigslist.com.mx', 'greensboro.craigslist.org', 'cairo.craigslist.org', 'marseilles.craigslist.org', 'florence.craigslist.it', 'ntl.craigslist.com.au', 'kenai.craigslist.org', 'detroit.craigslist.org', 'alicante.craigslist.es', 'ocala.craigslist.org', 'dunedin.craigslist.co.nz', 'tijuana.craigslist.com.mx', 'morgantown.craigslist.org', 'texoma.craigslist.org', 'bulgaria.craigslist.org', 'visalia.craigslist.org', 'soo.craigslist.ca', 'bajasur.craigslist.com.mx', 'nanjing.craigslist.com.cn', 'terrehaute.craigslist.org', 'york.craigslist.org', 'adelaide.craigslist.com.au', 'lancaster.craigslist.org', 'mexicocity.craigslist.com.mx', 'tucson.craigslist.org', 'colombia.craigslist.org', 'delrio.craigslist.org', 'ames.craigslist.org', 'hampshire.craigslist.co.uk', 'johannesburg.craigslist.co.za', 'quincy.craigslist.org', 'lubbock.craigslist.org', 'frankfurt.craigslist.de', 'valdosta.craigslist.org', 'surat.craigslist.co.in', 'ukraine.craigslist.org', 'kokomo.craigslist.org', 'bloomington.craigslist.org', 'yakima.craigslist.org', 'swks.craigslist.org', 'glensfalls.craigslist.org', 'yellowknife.craigslist.ca', 'delaware.craigslist.org', 'melbourne.craigslist.com.au', 'cornwall.craigslist.ca', 'malaga.craigslist.es', 'iowacity.craigslist.org', 'amarillo.craigslist.org', 'siouxfalls.craigslist.org', 'moseslake.craigslist.org', 'okaloosa.craigslist.org', 'kpr.craigslist.org', 'salem.craigslist.org', 'semo.craigslist.org', 'worcester.craigslist.org', 'loz.craigslist.org', 'chengdu.craigslist.com.cn', 'nwga.craigslist.org', 'modesto.craigslist.org', 'hiroshima.craigslist.jp', 'dublin.craigslist.org', 'kamloops.craigslist.ca', 'stuttgart.craigslist.de', 'christchurch.craigslist.org', 'mankato.craigslist.org', 'forums.craigslist.org', 'fortcollins.craigslist.org', 'greatfalls.craigslist.org', 'guatemala.craigslist.org', 'buenosaires.craigslist.org', 'ahmedabad.craigslist.co.in', 'rochester.craigslist.org', 'greenbay.craigslist.org', 'addisababa.craigslist.org', 'decatur.craigslist.org', 'albany.craigslist.org', 'venice.craigslist.it', 'raleigh.craigslist.org', 'redding.craigslist.org', 'pv.craigslist.com.mx', 'slo.craigslist.org', 'liverpool.craigslist.co.uk', 'showlow.craigslist.org', 'stgeorge.craigslist.org', 'up.craigslist.org', 'belohorizonte.craigslist.org', 'dubai.craigslist.org', 'fingerlakes.craigslist.org', 'tricities.craigslist.org', 'rockies.craigslist.org', 'windsor.craigslist.ca', 'bologna.craigslist.it', 'vancouver.craigslist.ca', 'eugene.craigslist.org', 'pullman.craigslist.org', 'sevilla.craigslist.es', 'centralmich.craigslist.org', 'topeka.craigslist.org', 'belleville.craigslist.ca', 'sudbury.craigslist.ca', 'anchorage.craigslist.org', 'boston.craigslist.org', 'spacecoast.craigslist.org', 'brownsville.craigslist.org', 'westmd.craigslist.org', 'maine.craigslist.org', 'sapporo.craigslist.jp', 'dusseldorf.craigslist.de', 'naga.craigslist.com.ph', 'ithaca.craigslist.org', 'meadville.craigslist.org', 'caribbean.craigslist.org', 'tokyo.craigslist.jp', 'myrtlebeach.craigslist.org', 'roswell.craigslist.org', 'stlouis.craigslist.org', 'baltimore.craigslist.org', 'orangecounty.craigslist.org', 'galveston.craigslist.org', 'reddeer.craigslist.ca', 'wollongong.craigslist.com.au', 'staugustine.craigslist.org', 'seoul.craigslist.co.kr', 'genoa.craigslist.it', 'bangkok.craigslist.co.th', 'tippecanoe.craigslist.org', 'portoalegre.craigslist.org', 'porthuron.craigslist.org', 'newjersey.craigslist.org', 'philadelphia.craigslist.org', 'quadcities.craigslist.org', 'iloilo.craigslist.com.ph', 'lasalle.craigslist.org', 'fayetteville.craigslist.org', 'seks.craigslist.org', 'kaiserslautern.craigslist.de', 'owensound.craigslist.ca', 'faro.craigslist.pt', 'hattiesburg.craigslist.org', 'beirut.craigslist.org', 'fortaleza.craigslist.org', 'harrisburg.craigslist.org', 'sierravista.craigslist.org', 'abilene.craigslist.org', 'huntsville.craigslist.org', 'sheffield.craigslist.co.uk', 'chihuahua.craigslist.com.mx', 'lynchburg.craigslist.org', 'columbus.craigslist.org', 'winchester.craigslist.org', 'southbend.craigslist.org', 'princegeorge.craigslist.ca', 'atlanta.craigslist.org', 'tehran.craigslist.org', 'cookeville.craigslist.org', 'wichitafalls.craigslist.org', 'nanaimo.craigslist.ca', 'norfolk.craigslist.org', 'ogden.craigslist.org', 'lethbridge.craigslist.ca', 'wv.craigslist.org', 'lincoln.craigslist.org', 'columbusga.craigslist.org', 'duluth.craigslist.org', 'smd.craigslist.org', 'charleston.craigslist.org', 'prescott.craigslist.org', 'pakistan.craigslist.org', 'comoxvalley.craigslist.ca', 'pei.craigslist.ca', 'victoriatx.craigslist.org', 'elpaso.craigslist.org', 'jacksontn.craigslist.org', 'okinawa.craigslist.jp', 'richmond.craigslist.org', 'edmonton.craigslist.ca', 'lyon.craigslist.org', 'newbrunswick.craigslist.ca', 'clovis.craigslist.org', 'louisville.craigslist.org', 'bordeaux.craigslist.org', 'minneapolis.craigslist.org', 'sanangelo.craigslist.org', 'jackson.craigslist.org', 'aberdeen.craigslist.co.uk', 'puebla.craigslist.com.mx', 'stockholm.craigslist.se', 'newlondon.craigslist.org', 'eastoregon.craigslist.org', 'monterrey.craigslist.com.mx', 'jerusalem.craigslist.org', 'eastnc.craigslist.org', 'cardiff.craigslist.co.uk', 'klamath.craigslist.org', 'casablanca.craigslist.org', 'montpellier.craigslist.org', 'canarias.craigslist.es', 'olympic.craigslist.org', 'humboldt.craigslist.org', 'dundee.craigslist.co.uk', 'santafe.craigslist.org', 'milwaukee.craigslist.org', 'burlington.craigslist.org', 'norwich.craigslist.co.uk', 'cairns.craigslist.com.au', 'lakeland.craigslist.org', 'istanbul.craigslist.com.tr', 'kenya.craigslist.org', 'bath.craigslist.co.uk', 'madrid.craigslist.es', 'madison.craigslist.org', 'fredericksburg.craigslist.org', 'williamsport.craigslist.org', 'abbotsford.craigslist.ca', 'scottsbluff.craigslist.org', 'moscow.craigslist.org', 'wilmington.craigslist.org', 'eastco.craigslist.org', 'athensohio.craigslist.org', 'southcoast.craigslist.org', 'bgky.craigslist.org', 'panamacity.craigslist.org', 'nh.craigslist.org', 'bern.craigslist.ch', 'phoenix.craigslist.org', 'skagit.craigslist.org', 'essen.craigslist.de', 'boulder.craigslist.org', 'hamilton.craigslist.ca', 'bham.craigslist.org', 'toulouse.craigslist.org', 'helena.craigslist.org', 'newhaven.craigslist.org', 'appleton.craigslist.org', 'chennai.craigslist.co.in', 'holland.craigslist.org', 'rio.craigslist.org', 'kalispell.craigslist.org', 'bhubaneswar.craigslist.co.in', 'strasbourg.craigslist.org', 'prague.craigslist.cz', 'athens.craigslist.gr', 'grandrapids.craigslist.org', 'bacolod.craigslist.com.ph', 'onslow.craigslist.org', 'helsinki.craigslist.fi', 'orlando.craigslist.org', 'davaocity.craigslist.com.ph', 'shreveport.craigslist.org', 'canberra.craigslist.com.au', 'newyork.craigslist.org', 'guanajuato.craigslist.com.mx', 'odessa.craigslist.org', 'dothan.craigslist.org', 'chautauqua.craigslist.org', 'amsterdam.craigslist.org', 'wheeling.craigslist.org', 'northmiss.craigslist.org', 'porto.craigslist.pt', 'baghdad.craigslist.org', 'thumb.craigslist.org', 'annapolis.craigslist.org', 'mobile.craigslist.org', 'springfield.craigslist.org', 'santiago.craigslist.org', 'chattanooga.craigslist.org', 'kalamazoo.craigslist.org', 'portland.craigslist.org', 'accra.craigslist.org', 'capecod.craigslist.org', 'danville.craigslist.org', 'durban.craigslist.co.za', 'charlotte.craigslist.org', 'dalian.craigslist.com.cn', 'cologne.craigslist.de', 'oaxaca.craigslist.com.mx', 'jacksonville.craigslist.org', 'wuhan.craigslist.com.cn', 'cariboo.craigslist.ca', 'mansfield.craigslist.org', 'brussels.craigslist.org', 'eauclaire.craigslist.org', 'hobart.craigslist.com.au', 'buffalo.craigslist.org', 'waco.craigslist.org', 'yuma.craigslist.org', 'allentown.craigslist.org', 'geneva.craigslist.ch', 'desmoines.craigslist.org', 'fairbanks.craigslist.org', 'sherbrooke.craigslist.ca', 'memphis.craigslist.org', 'bakersfield.craigslist.org', 'jakarta.craigslist.org', 'mumbai.craigslist.co.in', 'sendai.craigslist.jp', 'southjersey.craigslist.org', 'merced.craigslist.org', 'quebec.craigslist.ca', 'peterborough.craigslist.ca', 'brasilia.craigslist.org', 'medford.craigslist.org', 'bend.craigslist.org', 'longisland.craigslist.org', 'tuscaloosa.craigslist.org', 'nwks.craigslist.org', 'montevideo.craigslist.org', 'vienna.craigslist.at', 'sicily.craigslist.it', 'london.craigslist.co.uk', 'pensacola.craigslist.org', 'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'bremen.craigslist.de', 'copenhagen.craigslist.org', 'oregoncoast.craigslist.org', 'chongqing.craigslist.com.cn', 'chicago.craigslist.org', 'springfieldil.craigslist.org', 'veracruz.craigslist.com.mx', 'roseburg.craigslist.org', 'chambana.craigslist.org', 'florencesc.craigslist.org', 'washingtondc.craigslist.org', 'granada.craigslist.es', 'poconos.craigslist.org', 'winnipeg.craigslist.ca', 'berlin.craigslist.de', 'peace.craigslist.ca', 'cincinnati.craigslist.org', 'savannah.craigslist.org', 'reading.craigslist.org', 'stcloud.craigslist.org', 'kirksville.craigslist.org', 'gulfport.craigslist.org', 'meridian.craigslist.org', 'hyderabad.craigslist.co.in', 'bristol.craigslist.co.uk', 'lawrence.craigslist.org', 'tunis.craigslist.org', 'flagstaff.craigslist.org', 'recife.craigslist.org', 'missoula.craigslist.org', 'stpetersburg.craigslist.org', 'sheboygan.craigslist.org', 'chatham.craigslist.ca', 'rennes.craigslist.org', 'masoncity.craigslist.org', 'evansville.craigslist.org', 'monterey.craigslist.org', 'sanmarcos.craigslist.org', 'regina.craigslist.ca', 'elsalvador.craigslist.org', 'enid.craigslist.org', 'imperial.craigslist.org', 'quito.craigslist.org', 'troisrivieres.craigslist.ca', 'fortdodge.craigslist.org', 'edinburgh.craigslist.co.uk', 'sarnia.craigslist.ca', 'annarbor.craigslist.org', 'logan.craigslist.org', 'lakecharles.craigslist.org', 'lewiston.craigslist.org', 'warsaw.craigslist.pl', 'sfbay.craigslist.org', 'milan.craigslist.it', 'barcelona.craigslist.es', 'sydney.craigslist.com.au', 'janesville.craigslist.org', 'lisbon.craigslist.pt', 'cotedazur.craigslist.org', 'zurich.craigslist.ch', 'dubuque.craigslist.org', 'pune.craigslist.co.in', 'glasgow.craigslist.co.uk', 'zagreb.craigslist.org', 'shanghai.craigslist.com.cn', 'ottumwa.craigslist.org', 'indore.craigslist.co.in', 'potsdam.craigslist.org', 'hongkong.craigslist.hk', 'auckland.craigslist.org', 'westpalmbeach.craigslist.org', 'cdo.craigslist.com.ph', 'ottawa.craigslist.ca', 'telaviv.craigslist.org', 'pretoria.craigslist.co.za', 'rapidcity.craigslist.org', 'carbondale.craigslist.org', 'yubasutter.craigslist.org', 'cenla.craigslist.org', 'basel.craigslist.ch', 'fortmyers.craigslist.org', 'susanville.craigslist.org', 'omaha.craigslist.org', 'guangzhou.craigslist.com.cn', 'jerseyshore.craigslist.org', 'cranbrook.craigslist.ca', 'bilbao.craigslist.es', 'lapaz.craigslist.org', 'yucatan.craigslist.com.mx', 'ashtabula.craigslist.org', 'youngstown.craigslist.org', 'managua.craigslist.org', 'sacramento.craigslist.org', 'londonon.craigslist.ca', 'eastidaho.craigslist.org', 'altoona.craigslist.org', 'hudsonvalley.craigslist.org', 'twinfalls.craigslist.org', 'rouen.craigslist.org', 'saginaw.craigslist.org', 'dayton.craigslist.org', 'scranton.craigslist.org', 'rome.craigslist.it', 'valencia.craigslist.es', 'nagoya.craigslist.jp', 'jaipur.craigslist.co.in', 'elko.craigslist.org', 'billings.craigslist.org', 'boise.craigslist.org', 'mohave.craigslist.org', 'mcallen.craigslist.org', 'tallahassee.craigslist.org', 'butte.craigslist.org', 'wausau.craigslist.org', 'pennstate.craigslist.org', 'heidelberg.craigslist.de', 'manchester.craigslist.co.uk', 'bigbend.craigslist.org', 'collegestation.craigslist.org', 'peoria.craigslist.org', 'cedarrapids.craigslist.org', 'daytona.craigslist.org', 'montreal.craigslist.ca', 'spokane.craigslist.org', 'acapulco.craigslist.com.mx', 'calgary.craigslist.ca', 'kolkata.craigslist.co.in', 'goldcoast.craigslist.com.au', 'outerbanks.craigslist.org', 'lafayette.craigslist.org', 'saopaulo.craigslist.org', 'bangladesh.craigslist.org', 'juneau.craigslist.org', 'easttexas.craigslist.org', 'victoria.craigslist.ca', 'swmi.craigslist.org', 'stillwater.craigslist.org', 'fukuoka.craigslist.jp', 'mattoon.craigslist.org', 'utica.craigslist.org', 'vietnam.craigslist.org', 'tuscarawas.craigslist.org', 'clarksville.craigslist.org', 'bn.craigslist.org', 'hickory.craigslist.org', 'fresno.craigslist.org', 'hanford.craigslist.org', 'jxn.craigslist.org', 'malaysia.craigslist.org', 'whitehorse.craigslist.ca', 'hartford.craigslist.org', 'wenatchee.craigslist.org', 'huntington.craigslist.org', 'westky.craigslist.org', 'brantford.craigslist.ca', 'ventura.craigslist.org', 'toronto.craigslist.ca', 'delhi.craigslist.co.in', 'brisbane.craigslist.com.au', 'luxembourg.craigslist.org', 'inlandempire.craigslist.org', 'stjoseph.craigslist.org', 'manila.craigslist.com.ph', 'capetown.craigslist.co.za', 'sd.craigslist.org', 'frederick.craigslist.org', 'darwin.craigslist.com.au', 'lansing.craigslist.org', 'perth.craigslist.com.au', 'caracas.craigslist.org', 'derby.craigslist.co.uk', 'lexington.craigslist.org', 'grandforks.craigslist.org', 'reykjavik.craigslist.org', 'oslo.craigslist.org', 'houston.craigslist.org', 'santodomingo.craigslist.org', 'grenoble.craigslist.org', 'essex.craigslist.co.uk', 'munich.craigslist.de', 'chandigarh.craigslist.co.in', 'grandisland.craigslist.org', 'brainerd.craigslist.org', 'charlestonwv.craigslist.org', 'taipei.craigslist.com.tw', 'athensga.craigslist.org', 'northplatte.craigslist.org', 'westernmass.craigslist.org', 'battlecreek.craigslist.org', 'nesd.craigslist.org', 'auburn.craigslist.org', 'costarica.craigslist.org', 'www.craigslist.org', 'cadiz.craigslist.es', 'tulsa.craigslist.org', 'richmondin.craigslist.org', 'salina.craigslist.org', 'sunshine.craigslist.ca', 'nd.craigslist.org', 'bangalore.craigslist.co.in', 'honolulu.craigslist.org', 'skeena.craigslist.ca', 'chambersburg.craigslist.org', 'providence.craigslist.org', 'catskills.craigslist.org', 'hermosillo.craigslist.com.mx', 'charlottesville.craigslist.org', 'indianapolis.craigslist.org', 'farmington.craigslist.org', 'bozeman.craigslist.org', 'guelph.craigslist.ca', 'oxford.craigslist.co.uk', 'baleares.craigslist.es', 'juarez.craigslist.com.mx', 'martinsburg.craigslist.org', 'lascruces.craigslist.org', 'kent.craigslist.co.uk', 'belfast.craigslist.co.uk', 'barrie.craigslist.ca', 'beaumont.craigslist.org', 'texarkana.craigslist.org', 'waterloo.craigslist.org', 'nmi.craigslist.org', 'sarasota.craigslist.org', 'kansascity.craigslist.org', 'northernwi.craigslist.org', 'kelowna.craigslist.ca', 'thunderbay.craigslist.ca', 'columbia.craigslist.org', 'kuwait.craigslist.org', 'torino.craigslist.it', 'cambridge.craigslist.co.uk', 'osaka.craigslist.jp', 'devon.craigslist.co.uk', 'monroe.craigslist.org', 'santabarbara.craigslist.org', 'montana.craigslist.org', 'oneonta.craigslist.org', 'panama.craigslist.org', 'montgomery.craigslist.org', 'hangzhou.craigslist.com.cn', 'leeds.craigslist.co.uk', 'miami.craigslist.org', 'fortlauderdale.craigslist.org', 'macon.craigslist.org', 'goa.craigslist.co.in', 'guadalajara.craigslist.com.mx', 'micronesia.craigslist.org', 'batonrouge.craigslist.org', 'niagara.craigslist.ca', 'blacksburg.craigslist.org', 'elmira.craigslist.org', 'fortwayne.craigslist.org', 'eastky.craigslist.org', 'kerala.craigslist.co.in', 'saguenay.craigslist.ca', 'twintiers.craigslist.org', 'lausanne.craigslist.ch', 'rmn.craigslist.org', 'palmsprings.craigslist.org', 'gadsden.craigslist.org', 'bismarck.craigslist.org', 'monroemi.craigslist.org', 'halifax.craigslist.ca', 'lasvegas.craigslist.org', 'columbiamo.craigslist.org', 'greenville.craigslist.org', 'akroncanton.craigslist.org', 'provo.craigslist.org', 'owensboro.craigslist.org', 'treasure.craigslist.org', 'siskiyou.craigslist.org', 'killeen.craigslist.org', 'tampa.craigslist.org', 'easternshore.craigslist.org', 'wyoming.craigslist.org', 'cleveland.craigslist.org', 'fayar.craigslist.org', 'corvallis.craigslist.org', 'saskatoon.craigslist.ca', 'sandusky.craigslist.org', 'zanesville.craigslist.org', 'singapore.craigslist.com.sg', 'nashville.craigslist.org', 'hannover.craigslist.de', 'lucknow.craigslist.co.in', 'littlerock.craigslist.org', 'brunswick.craigslist.org', 'saltlakecity.craigslist.org', 'wichita.craigslist.org', 'fortsmith.craigslist.org', 'swva.craigslist.org', 'leipzig.craigslist.de', 'loire.craigslist.org', 'ftmcmurray.craigslist.ca', 'chico.craigslist.org', 'bellingham.craigslist.org', 'fargo.craigslist.org', 'cnj.craigslist.org', 'cfl.craigslist.org', 'watertown.craigslist.org', 'laredo.craigslist.org', 'newfoundland.craigslist.ca', 'augusta.craigslist.org', 'mendocino.craigslist.org', 'coventry.craigslist.co.uk', 'pueblo.craigslist.org', 'lacrosse.craigslist.org', 'binghamton.craigslist.org', 'boone.craigslist.org', 'csd.craigslist.org', 'lakecity.craigslist.org', 'albuquerque.craigslist.org', 'budapest.craigslist.org', 'shenzhen.craigslist.com.cn', 'naples.craigslist.it', 'asheville.craigslist.org', 'ksu.craigslist.org', 'dallas.craigslist.org', 'wellington.craigslist.org', 'beijing.craigslist.com.cn', 'losangeles.craigslist.org', 'harrisonburg.craigslist.org', 'sardinia.craigslist.it', 'muskegon.craigslist.org', 'pampanga.craigslist.com.ph', 'gainesville.craigslist.org', 'sanantonio.craigslist.org', 'ramallah.craigslist.org', 'chillicothe.craigslist.org', 'goldcountry.craigslist.org', 'territories.craigslist.ca', 'hat.craigslist.ca', 'toledo.craigslist.org', 'flint.craigslist.org', 'lawton.craigslist.org', 'muncie.craigslist.org', 'statesboro.craigslist.org', 'erie.craigslist.org', 'limaohio.craigslist.org', 'corpuschristi.craigslist.org', 'parkersburg.craigslist.org', 'pittsburgh.craigslist.org', 'racine.craigslist.org', 'oklahomacity.craigslist.org', 'bucharest.craigslist.org', 'plattsburgh.craigslist.org', 'shenyang.craigslist.com.cn', 'dresden.craigslist.de', 'sandiego.craigslist.org', 'bemidji.craigslist.org', 'stockton.craigslist.org', 'perugia.craigslist.it', 'seattle.craigslist.org', 'curitiba.craigslist.org', 'santamaria.craigslist.org', 'keys.craigslist.org', 'kitchener.craigslist.ca', 'siouxcity.craigslist.org', 'hamburg.craigslist.de', 'denver.craigslist.org', 'houma.craigslist.org', 'rockford.craigslist.org', 'marshall.craigslist.org', 'swv.craigslist.org', 'eastmids.craigslist.co.uk', 'nacogdoches.craigslist.org', 'neworleans.craigslist.org', 'brighton.craigslist.co.uk', 'salvador.craigslist.org', 'natchez.craigslist.org', 'lima.craigslist.org', 'syracuse.craigslist.org', 'nwct.craigslist.org', 'paris.craigslist.org', 'joplin.craigslist.org', 'whistler.craigslist.ca', 'kingston.craigslist.ca', 'nuremberg.craigslist.de', 'roanoke.craigslist.org', 'reno.craigslist.org', 'birmingham.craigslist.co.uk', 'westslope.craigslist.org', 'lille.craigslist.org', 'haifa.craigslist.org', 'winstonsalem.craigslist.org', 'knoxville.craigslist.org', 'puertorico.craigslist.org', 'austin.craigslist.org', 'jonesboro.craigslist.org', 'shoals.craigslist.org'}
    assert_set_equal(observed, expected)
