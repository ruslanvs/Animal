class Animal( object ):
    def __init__( self, name = "-", health = 100 ):
        self.name = name
        self.health = health
        print "------ New animal has been created -------"
    def walk( self ):
        self.health -= 1
        print "Walk... -1 in health"
        return self
    def run( self ):
        self.health -= 5
        print "run... -5 in health"
        return self
    def display_health( self ):
        print "health level:", self.health
        return self

class Dog( Animal ):
    def __init__( self, health = 150 ):
        super( Dog, self ).__init__()
        self.health = health
        
    def pet( self ):
        self.health += 5
        print "pet... +5 in health"
        return self

class Dragon( Animal ):
    def __init__( self, health = 170 ):
        super( Dragon, self ).__init__()
        self.health = health
        
    def fly( self ):
        self.health -= 10
        print "Fly... -10 in health"
        return self

    def display_health( self ):
        super( Dragon, self ).display_health()
        print "I am a dragon"
        return self

dog1 = Dog( )

dog1.display_health().walk().walk().walk().run().pet().display_health()

dragon1 = Dragon()
dragon1.display_health().fly().fly().fly().display_health()

animal1 = Animal()
animal1.display_health()

# animal1.display_health().pet() just as expected - not working
# animal1.display_health().fly() just as expected - not working