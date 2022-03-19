import program.model as script
import pytest

# - Agent : 
class Agent:
    AGENT = script.Agent(30, agreeableness=1)
    #   - modifier un attribut position
    def test_modify_position(self):
        agent = self.AGENT
        agent.position = 5
        assert agent.position == 5
        
    #   - récupérer un attribut position
    def test_get_position(self):
        agent = self.AGENT
        assert agent.position == 30
    
    #   - assigner un dictionnaire en tant qu'attributs
    def test_set_agent_attributes(self):
        agent = self.AGENT
        assert agent.agreeableness == 1

# - Position :
class Position:
    POSITION = script.Position(100, 34)
    #   - modifier un attribut longitude_degrees
    def test_longitude_degrees(self):
        position =self.POSITION
        assert position.longitude_degrees == 100
        
    #   - modifier un attribut latitude_degrees
    def test_latitude_degrees(self):
        position = self.POSITION
        assert position.latitude_degrees == 34
    
    #   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
    def test_longitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = script.Position(200, 33)

    #   - modifier un attribut latitude_degrees avec une valeur supérieure à 90 renvoie une erreur. 
    def test_latitude_degrees_range(self):
        with pytest.raises(AssertionError):
            position = script.Position(100, 100)

    #   - récupérer une latitude
    def test_latitude(self):
        position = self.POSITION
        # print(position.latitude)
        assert position.latitude == 0.5934119456780721
        
    #   - récupérer une longitude
    def test_longitude(self):
        position = self.POSITION
        # print(position.longitude)
        assert position.longitude == 1.7453292519943295

# - Zone :
class TestZone:
    POSITION1 = script.Position(100, 33)
    POSITION2 = script.Position(101, 34)
    ZONE = script.Zone(POSITION1, POSITION2)
    AGENT = script.Agent(POSITION1, agreeableness=1)
    
    #   - trouver une zone qui contient une position
    def test_find_zone_that_contains(self):
        found_zone = script.Zone.find_zone_that_contains(self.POSITION1)
        assert found_zone.corner1.longitude == self.ZONE.corner1.longitude

    #   - ajouter un habitant dans une zone
    def test_add_inhabitant_in_zone(self):
        self.ZONE.add_inhabitant(self.AGENT)
        assert len(self.ZONE.inhabitants) == 1

    #   - récupérer toutes les instances Zone (Zone.ZONES)
    # On devrait avoir exactement 64800 zones
    def test_get_zones(self):
        assert len(script.Zone.ZONES) == 64800
        # print(len(script.Zone.ZONES))

    #   - récupérer la densité de population d'une zone
    def test_get_population_density(self):
        assert self.ZONE.population_density() == 8.087793508722422e-05

    #   - récupérer l'agréabilité moyenne d'une zone
    def test_get_average_agreeableness(self):
        assert self.ZONE.average_agreeableness() == 1

# - AgreeablenessGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est la densité de population moyenne
#   - la seconde valeur de xy_values est l'agréabilité moyenne

# - IncomeGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est l'âge
#   - la seconde valeur de xy_values est le revenu