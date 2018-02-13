from .cards_object import CardsObject
import urllib.parse

class Search(CardsObject):
	def __init__(self, **kwargs):
		self.q = kwargs.get('q', 'None')
		self.order = kwargs.get('order', 'None')
		self.unique = kwargs.get('unique', 'False')
		self.dir = kwargs.get('dir', 'Auto')
		self.include_extras = kwargs.get('include_extras', 'False')
		self.page = kwargs.get('page', '1')
		self.dict = {
			'q':self.q,
			'order':self.order,
			'unique':self.unique,
			'dir':self.dir,
			'include_extras':self.include_extras,
			'page':self.page
			}

		self.args = urllib.parse.urlencode(self.dict)
		self.url = 'cards/search?' + self.args

		super(Search, self).__init__(self.url)

	def __checkForKey(self, key):
		try:
			return self.scryfallJson[key]
		except KeyError:
			return None

	def object(self):
		if self.__checkForKey('object') is None:
			raise KeyError('This object has no key \'object\'')

		return self.scryfallJson['object']

	def total_cards(self):
		if self.__checkForKey('total_cards') is None:
			raise KeyError('This object has no key \'total_cards\'')

		return self.scryfallJson['total_cards']

	def data(self):
		if self.__checkForKey('data') is None:
			raise KeyError('This object has no key \'data\'')

		return self.scryfallJson['data']

	def next_page(self):
		if self.__checkForKey('next_page') is None:
			raise KeyError('This object has no key \'next_page\'')

		return self.scryfallJson['next_page']

	def warnings(self):
		if self.__checkForKey('warnings') is None:
			raise KeyError('This object has no key \'warnings\'')

		return self.scryfallJson['warnings']

	#The following attributes are only to override the inherited class attributes.
	#This class has no matching attributes but we still need the getRequest function from CardsObject

	def id(self):
		raise AttributeError('Search object has no attribute \'id\'')

	def multiverse_ids(self):
		raise AttributeError('Search object has no attribute \'multiverse_ids\'')

	def mtgo_id(self):
		raise AttributeError('Search object has no attribute \'mtgo_id\'')

	def mtgo_foil_id(self):
		raise AttributeError('Search object has no attribute \'mtgo_foil_id\'')

	def name(self):
		raise AttributeError('Search object has no attribute \'name\'')

	def uri(self):
		raise AttributeError('Search object has no attribute \'uri\'')

	def scryfall_uri(self):
		raise AttributeError('Search object has no attribute \'scryfall_uri\'')

	def layout(self):
		raise AttributeError('Search object has no attribute \'layout\'')

	def highres_image(self):
		raise AttributeError('Search object has no attribute \'highres_image\'')

	def image_uris(self):
		raise AttributeError('Search object has no attribute \'image_uris\'')

	def cmc(self):
		raise AttributeError('Search object has no attribute \'cmc\'')

	def type_line(self):
		raise AttributeError('Search object has no attribute \'type_line\'')

	def oracle_text(self):
		raise AttributeError('Search object has no attribute \'oracle_text\'')

	def mana_cost(self):
		raise AttributeError('Search object has no attribute \'mana_cost\'')

	def colors(self):
		raise AttributeError('Search object has no attribute \'colors\'')

	def color_identity(self):
		raise AttributeError('Search object has no attribute \'color_identity\'')

	def legalities(self):
		raise AttributeError('Search object has no attribute \'legalities\'')

	def reserved(self):
		raise AttributeError('Search object has no attribute \'reserved\'')

	def reprint(self):
		raise AttributeError('Search object has no attribute \'reprint\'')

	def set_code(self):
		raise AttributeError('Search object has no attribute \'	def set_code\'')

	def set_name(self):
		raise AttributeError('Search object has no attribute \'	def set_name\'')

	def set_uri(self):
		raise AttributeError('Search object has no attribute \'set_uri\'')

	def set_search_uri(self):
		raise AttributeError('Search object has no attribute \'set_search_uri\'')

	def scryfall_set_uri(self):
		raise AttributeError('Search object has no attribute \'scryfall_set_uri\'')

	def rulings_uri(self):
		raise AttributeError('Search object has no attribute \'rulings_uri\'')

	def prints_search_uri(self):
		raise AttributeError('Search object has no attribute \'prints_search_uri\'')

	def collector_number(self):
		raise AttributeError('Search object has no attribute \'collector_number\'')

	def digital(self):
		raise AttributeError('Search object has no attribute \'digital\'')

	def rarity(self):
		raise AttributeError('Search object has no attribute \'rarity\'')

	def illustration_id(self):
		raise AttributeError('Search object has no attribute \'illustration_id\'')

	def artist(self):
		raise AttributeError('Search object has no attribute \'artist\'')

	def frame(self):
		raise AttributeError('Search object has no attribute \'frame\'')

	def full_art(self):
		raise AttributeError('Search object has no attribute \'full_art\'')

	def border_color(self):
		raise AttributeError('Search object has no attribute \'border_color\'')

	def timeshifted(self):
		raise AttributeError('Search object has no attribute \'timeshifted\'')

	def colorshifted(self):
		raise AttributeError('Search object has no attribute \'colorshifted\'')

	def futureshifted(self):
		raise AttributeError('Search object has no attribute \'futureshifted\'')

	def edhrec_rank(self):
		raise AttributeError('Search object has no attribute \'edhrec_rank\'')

	def currency(self, mode):
		raise AttributeError('Search object has no attribute \'currency(self,\'')

	def related_uris(self):
		raise AttributeError('Search object has no attribute \'related_uris\'')

	def purchase_uris(self):
		raise AttributeError('Search object has no attribute \'purchase_uris\'')

	def life_modifier(self):
		raise AttributeError('Search object has no attribute \'life_modifier\'')

	def hand_modifier(self):
		raise AttributeError('Search object has no attribute \'hand_modifier\'')

	def color_indicator(self):
		raise AttributeError('Search object has no attribute \'color_indicator\'')

	def all_parts(self):
		raise AttributeError('Search object has no attribute \'all_parts\'')

	def card_faces(self):
		raise AttributeError('Search object has no attribute \'card_faces\'')

	def watermark(self):
		raise AttributeError('Search object has no attribute \'watermark\'')

	def story_spotlight_number(self):
		raise AttributeError('Search object has no attribute \'story_spotlight_number\'')

	def story_spotlight_uri(self):
		raise AttributeError('Search object has no attribute \'story_spotlight_uri\'')
