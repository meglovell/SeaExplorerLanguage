import random
from PIL import Image, ImageDraw, ImageFont

from os.path import dirname, join

from textx import metamodel_from_file
from textx.export import metamodel_export, model_export


class SeaExplorer:

    def __init__(self):
        #distanceCount keeps track of total swimming distance, depthCount keeps track of total diving depth
        #distance keeps track of current swimming distance, depth keeps track of current diving depth
        #seaCreatureCount keeps track of total sea creatures discovered
        self.distanceCount = 0
        self.depthCount = 0
        self.distance = 0
        self.depth = 0
        self.seaCreatureCount = 0

    def __str__(self):
        return f"Sea Explorer"
    
    
    def interpret(self, program):

        #program is an instance of Program in BNF
        for act in program.actions:


            #manages the total and current swimming distances
            if act.__class__.__name__ == "Swim":
                self.distance += act.distance
                self.distanceCount += act.distance

                if self.distance <= 2000:
                    print(f"Swimming distance so far is", self.distance, "yard(s)")
                else:
                    print(f"Maximum swimming distance at one time is 2000 yards")
                    quit()

            #manages the total and current diving depths
            elif act.__class__.__name__ == "Dive":
                self.depth += act.depth
                self.depthCount += act.depth
                
                if self.depth <= 300:
                    print(f"Diving depth so far is", self.depth, "yard(s)")
                else:
                    print(f"Maximum diving depth at one time is 300 yards")
                    quit()

            #manages discoveries at different diving depths
            elif act.__class__.__name__ == "Discovery":

                if self.depth in range(0, 6):
                    
                    seaCreatureList1 = ["Leafy Seadragon", "Garden Eel", "Jellyfish", "Sea Otter", "Green Moray Eel"]
                    seaCreature = random.choice(seaCreatureList1)
                    print(f"You have found a(n) " + seaCreature + "!")
                    self.seaCreatureCount += 1


                    if seaCreature == "Leafy Seadragon":
                        img = Image.open('LeafySeadragon.jpg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: seagrass beds, rocky reefs, southern Australian coast"
                        draw.text((10, 450), caption, fill="white", font=font)
                        img.show()


                    if seaCreature == "Garden Eel":
                        img = Image.open('GardenEel.jpg')
                        img_resized = img.resize((400, 300))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: sandy flats, among seagrass, warm ocean waters like Indo-Pacific"
                        draw.text((10, 280), caption, fill="white", font=font)
                        img_resized.show()


                    if seaCreature == "Jellyfish":
                        img = Image.open('Jellyfish.jpg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: warm and cold climates, storms can push them into deep waters"
                        draw.text((10, 380), caption, fill="white", font=font)
                        img.show()

                        #danger adjustment
                        print(f"Might be friendly, might not be - swimming distance increased by 2 yards to avoid danger")
                        self.distance += 2
                        self.distanceCount = self.distance


                    if seaCreature == "Sea Otter":
                        img = Image.open('SeaOtter.jpg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='black', font=font)
                        caption = "Habitat: rocky shores, kelp forests, warm to sub-polar climates in north Pacific Ocean"
                        draw.text((10, 350), caption, fill="black", font=font)
                        img.show()


                    if seaCreature == "Green Moray Eel":
                        img = Image.open('GreenMorayEel.jpg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coral reefs, mangroves, found in Bahamas and Florida Keys"
                        draw.text((10, 450), caption, fill="black", font=font)
                        img.show()

                        #danger adjustment
                        print(f"Caution - swimming distance increased by 4 yards to avoid danger")
                        self.distance += 4
                        self.distanceCount = self.distance


                elif self.depth in range(6, 50):
                    
                    seaCreatureList2 = ["Dolphin", "Loggerhead Turtle", "Whale Shark", "Great White Shark", "Orca"]
                    seaCreature = random.choice(seaCreatureList2)
                    print(f"You have found a(n) " + seaCreature + "!")
                    self.seaCreatureCount += 1


                    if seaCreature == "Dolphin":
                        img = Image.open('Dolphin.webp')
                        img_resized = img.resize((600, 400))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coastal to open ocean, tropical to sub-polar climates"
                        draw.text((10, 380), caption, fill="white", font=font)
                        img_resized.show()
                    

                    if seaCreature == "Loggerhead Turtle":
                        img = Image.open('LoggerheadTurtle.jpeg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coastal to open ocean, tropical temperatures"
                        draw.text((10, 150), caption, fill="white", font=font)
                        img.show()


                    if seaCreature == "Whale Shark":
                        img = Image.open('WhaleShark.jpg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coastal to open ocean, specific reefs and beaches, tropical climates"
                        draw.text((10, 270), caption, fill="white", font=font)
                        img.show()
                    

                    if seaCreature == "Great White Shark":
                        img = Image.open('GreatWhiteShark.jpeg')
                        img_resized = img.resize((500, 300))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coastal to open ocean, tropical to cold climates"
                        draw.text((10, 280), caption, fill="white", font=font)
                        img_resized.show()

                        #danger adjustment
                        print(f"Caution - swimming distance increased by 5 yards to avoid danger")
                        self.distance += 5
                        self.distanceCount = self.distance

                    
                    if seaCreature == "Orca":
                        img = Image.open('Orca.jpg')
                        img_resized = img.resize((600, 400))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: coastal to open ocean, global - all climates in the ocean"
                        draw.text((10, 380), caption, fill="white", font=font)
                        img_resized.show()

                        #danger adjustment
                        print(f"Caution - diving depth decreased by 3 yards to avoid danger")
                        self.depthCount = self.depth
                        self.depth -= 3


                elif self.depth in range(50, 301):
                    
                    seaCreatureList3 = ["Sea Angel", "Flapjack Octopus", "Anglerfish", "Colossal Squid", "Pacific Blackdragon"]
                    seaCreature = random.choice(seaCreatureList3)
                    print(f"You have found a(n) " + seaCreature + "!")
                    self.seaCreatureCount += 1


                    if seaCreature == "Sea Angel":
                        img = Image.open('SeaAngel.webp')
                        img_resized = img.resize((400, 600))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: temperate to cold waters, found worldwide"
                        draw.text((10, 580), caption, fill="white", font=font)
                        img_resized.show()


                    if seaCreature == "Flapjack Octopus":
                        img = Image.open('FlapjackOctopus.jpg')
                        img_resized = img.resize((600, 400))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='black', font=font)
                        caption = "Habitat: deep open ocean, global - tropical to temperate climates"
                        draw.text((10, 380), caption, fill="black", font=font)
                        img_resized.show()


                    if seaCreature == "Anglerfish":
                        img = Image.open('Anglerfish.jpg')
                        img_resized = img.resize((600, 400))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: deep sea, open ocean, global - tropical to temperate climates"
                        draw.text((10, 380), caption, fill="white", font=font)
                        img_resized.show()

                        #danger adjustment
                        print(f"Danger - swim away!")
                        self.distanceCount = self.distance
                        self.distance = 0
                        self.depthCount = self.depth
                        self.depth = 0
                        print(f"Your current swimming distance and current diving depth are now", self.distance, "yards and", self.depth, "yards")


                    if seaCreature == "Colossal Squid":
                        img = Image.open('ColossalSquid.jpeg')
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: open ocean, polar climates around Antarctica and in the Southern Ocean"
                        draw.text((10, 300), caption, fill="white", font=font)
                        img.show()

                        #danger adjustment
                        print(f"Caution - diving depth decreased by 30 yards to avoid danger")
                        self.depthCount = self.depth
                        self.depth -= 30


                    if seaCreature == "Pacific Blackdragon":
                        img = Image.open('PacificBlackdragon.jpeg')
                        img_resized = img.resize((500, 300))
                        draw = ImageDraw.Draw(img_resized)
                        font = ImageFont.load_default()
                        draw.text((10, 10), seaCreature, fill='white', font=font)
                        caption = "Habitat: deep sea, open ocean, Eastern Pacific Ocean from California to Chile"
                        draw.text((10, 380), caption, fill="white", font=font)
                        img_resized.show()

                        #danger adjustment
                        print(f"Danger - swim away!")
                        self.distanceCount = self.distance
                        self.distance = 0
                        self.depthCount = self.depth
                        self.depth = 0
                        print(f"Your current swimming distance and current diving depth are now", self.distance, "yards and", self.depth, "yards")

            
            print(self)
        
        print("Your total swimming distance is", self.distanceCount, "and your total diving depth is", self.depthCount)
        print("You have discovered", self.seaCreatureCount, "sea creature(s)!")
        print(f"You have found", self.seaCreatureCount * 100, "gold coins for finding", self.seaCreatureCount, "sea creatures!")

        
        if self.seaCreatureCount == 0:
            img = Image.open('Treasure.jpg')
            draw = ImageDraw.Draw(img)
            img_gray = img.convert('L')
            img_gray.show()

        for x in range(self.seaCreatureCount):
            
            img = Image.open('Treasure.jpg')
            draw = ImageDraw.Draw(img)
            img.show()
                
            



def main(debug=False):

    this_folder = dirname(__file__)

    SeaExplorer_mm = metamodel_from_file(join(this_folder, 'SeaExplorer.tx'), debug=False)
    metamodel_export(SeaExplorer_mm, join(this_folder, 'SeaExplorer_meta.dot'))

    #making models from the textX file
    SeaExplorer_model1 = SeaExplorer_mm.model_from_file(join(this_folder, 'sample1.SE'))
    model_export(SeaExplorer_model1, join(this_folder, 'SEprogram1.dot'))

    SeaExplorer_model2 = SeaExplorer_mm.model_from_file(join(this_folder, 'sample2.SE'))
    model_export(SeaExplorer_model2, join(this_folder, 'SEprogram2.dot'))

    SeaExplorer_model3 = SeaExplorer_mm.model_from_file(join(this_folder, 'sample3.SE'))
    model_export(SeaExplorer_model3, join(this_folder, 'SEprogram3.dot'))

    #interpreting the 3 sample programs
    seaExplorer1 = SeaExplorer()
    seaExplorer1.interpret(SeaExplorer_model1)
    print()

    seaExplorer2 = SeaExplorer()
    seaExplorer2.interpret(SeaExplorer_model2)
    print()

    seaExplorer3 = SeaExplorer()
    seaExplorer3.interpret(SeaExplorer_model3)
    print()


if __name__ == "__main__":
    main()

