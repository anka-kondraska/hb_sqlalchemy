"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corv_models = Model.query.filter_by(name='Corvette', brand_name='Chevrolet')

# Get all models that are older than 1960.
sixty = Model.query.filter(Model.year<1960)

# Get all brands that were founded after 1920.
twenty = Brand.query.filter(Brand.founded>1920)

# Get all models with names that begin with "Cor".
cor = Model.query.filter(Model.name.like('Cor%'))

# Get all brands that were founded in 1903 and that are not yet discontinued.
othree = Brand.query.filter((Brand.founded==1903), (Brand.discontinued==None))


# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
disc = Brand.query.filter( (Brand.discontinued!=None) | (Brand.founded<1950) )


# Get all models whose brand_name is not Chevrolet.
chev = Model.query.filter(Model.brand_name!='Chevrolet')


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    all_m = db.session.query(Model.year, Model.name, Model.brand_name, Brand.headquarters).join(Brand).all()
    for m_year, name, brand_name, headquarters in all_m:
        if m_year == year:
            print name, brand_name, headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_b = db.session.query(Model).order_by(Model.brand_name)

    for orb in all_b:
        print orb.brand_name, orb.name 
        print

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The returned value is <flask_sqlalchemy.BaseQuery object at 0x7f36898bde10>
# and the returned datatype is object.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# bridge table, cross-reference table, crosswalk, intermediary table, 
# intersection table, join table, junction table, link table, linking table, 
# many-to-many resolver, map table, mapping table, pairing table, or transition table
#
# many to one relationship between the associative table and data tables
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """takes in any string as parameter, and returns a list of 
    objects that are brands whose name contains or is equal 
    to the input string"""

    mystr = "%"+mystr+"%"

    str_brands = Model.query.filter(Model.brand_name.like(mystr))
    for brands in str_brands:
        print brands


def get_models_between(start_year, end_year):
    """takes in a start year and end year (two integers), and returns 
    a list of objects that are models with years that fall between t
    he start year (inclusive) and end year (exclusive)."""

    model_range = Model.query.filter((Model.year>(start_year-1)),(Model.year<(end_year+1)))
    for model in model_range:
        print model

