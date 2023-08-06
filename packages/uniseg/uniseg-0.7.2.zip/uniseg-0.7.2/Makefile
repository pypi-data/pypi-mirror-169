.PHONY: clean test upload docs db_lookups testpypi pypi

PROJ_NAME = uniseg

MKDIR = "mkdir"
MV = mv
RM = rm -v
CURL = curl --compressed
PYTHON = python
PIP = pip
SPHINX_BUILD = sphinx-build

UNICODE_VERSION = 6.2.0
URL_DOWNLOAD = http://www.unicode.org/Public/$(UNICODE_VERSION)/ucd
DIR_DOWNLOAD = data/$(UNICODE_VERSION)
DIR_SRC = uniseg
DIR_DIST = dist
DB_LOOKUPS = $(DIR_SRC)/db_lookups.py
DB_LOOKUPS_TEST = $(DIR_SRC)/db_lookups_test.py
DIR_DOCS = docs
DIR_DOCS_BUILD = docs/_build

CSV_FILES =\
    csv/GraphemeClusterBreak.csv\
    csv/GraphemeClusterBreakTest.csv\
    csv/WordBreak.csv\
    csv/WordBreakTest.csv\
    csv/SentenceBreak.csv\
    csv/SentenceBreakTest.csv\
    csv/LineBreak.csv\
    csv/LineBreakTest.csv

test: db_lookups
	$(PYTHON) -m $(DIR_SRC).test

db_lookups: $(CSV_FILES)
	$(PYTHON) tools/build_db_lookups.py
	$(PYTHON) tools/build_db_lookups_test.py

clean:
	-$(RM) $(DIR_SRC)/*.pyc
	-$(RM) -r csv

cleanall: clean cleandocs
	-$(RM) $(DB_LOOKUPS)
	-$(RM) $(DB_LOOKUPS_TEST)
	-$(RM) -r $(DIR_DOWNLOAD)
	-$(RM) MANIFEST
	-$(RM) -r dist
	-$(RM) -r data
	-$(RM) -r build

sdist: db_lookups
	$(PYTHON) setup.py sdist -d $(DIR_DIST) --formats=zip

wheel: db_lookups
	$(PYTHON) setup.py bdist_wheel -d $(DIR_DIST) --universal

testpypi: sdist wheel
	twine upload -r testpypi --skip-existing dist/*

pypi: sdist wheel
	twine upload dist/*

install:
	$(PIP) install -e .

docs:
	$(SPHINX_BUILD) -b html $(DIR_DOCS) $(DIR_DOCS_BUILD)/html

cleandocs:
	-$(RM) -r $(DIR_DOCS_BUILD)

csv/GraphemeClusterBreak.csv: $(DIR_DOWNLOAD)/auxiliary/GraphemeBreakProperty.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/prop2csv.py -o $@ $<

csv/GraphemeClusterBreakTest.csv: $(DIR_DOWNLOAD)/auxiliary/GraphemeBreakTest.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/test2csv.py -p GB -o $@ $<

csv/WordBreak.csv: $(DIR_DOWNLOAD)/auxiliary/WordBreakProperty.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/prop2csv.py -o $@ $<

csv/WordBreakTest.csv: $(DIR_DOWNLOAD)/auxiliary/WordBreakTest.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/test2csv.py -p WB -o $@ $<

csv/SentenceBreak.csv: $(DIR_DOWNLOAD)/auxiliary/SentenceBreakProperty.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/prop2csv.py -o $@ $^

csv/SentenceBreakTest.csv: $(DIR_DOWNLOAD)/auxiliary/SentenceBreakTest.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/test2csv.py -p SB -o $@ $<

csv/LineBreak.csv: $(DIR_DOWNLOAD)/LineBreak.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/prop2csv.py -o $@ $^

csv/LineBreakTest.csv: $(DIR_DOWNLOAD)/auxiliary/LineBreakTest.txt
	-$(MKDIR) -p $(dir $@)
	$(PYTHON) tools/test2csv.py -p LB -o $@ $<

# Use 'mkdir -p' instead of --create-dirs option of curl because it
# doesn't work well with path names with '/' on Windows.
$(DIR_DOWNLOAD)/%:
	-$(MKDIR) -p $(dir $@)
	$(CURL) -o $@ $(subst $(DIR_DOWNLOAD),$(URL_DOWNLOAD),$@)
