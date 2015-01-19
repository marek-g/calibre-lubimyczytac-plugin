#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__   = 'GPL v3'
__copyright__ = '2015, Marek Gibek'
__docformat__ = 'restructuredtext en'

from calibre import as_unicode, browser
from calibre.ebooks.metadata.book.base import Metadata
from calibre.ebooks.metadata.sources.base import Source

class LubimyCzytac(Source):
	name                    = 'LubimyCzytac'
	description             = _('Downloads metadata and covers from LubimyCzytac.pl')
	author                  = 'Marek Gibek'
	version                 = (1, 0, 0)
	minimum_calibre_version = (0, 8, 15)

	capabilities = frozenset(['identify', 'cover'])
	touched_fields = frozenset(['title', 'authors', 'identifier:lubimyczytac', 'identifier:isbn', 'rating', 'comments', 'publisher', 'pubdate', 'series', 'series_index', 'tags', 'languages'])
	has_html_comments = True
	supports_gzip_transfer_encoding = True

	def identify(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
		matches = []

		mi = Metadata(title, authors)
		mi.comments = "Comment1"
		result_queue.put(mi)

		query = self.create_query(log, title=title, authors=authors, identifiers=identifiers)
		if query is None:
			log.error('Insufficient metadata to construct query')
			return

		log.info('Query phase: ' + query)

		mi = Metadata(title, authors)
		mi.comments = query
		result_queue.put(mi)


	def create_query(self, log, title=None, authors=None, identifiers={}):
		print ('create_query')
		q = ''
		if title:
			tokens = list(self.get_title_tokens(title, strip_joiners=False, strip_subtitle=True))
		else:
			tokens = list(self.get_author_tokens(title, only_first_author=True))

		q = '+'.join(tokens)
		if not q:
			return None

		print ('q')
		print (q)
		url ='http://lubimyczytac.pl/searcher/getsuggestions?phrase=' + q
		return url.lower()
