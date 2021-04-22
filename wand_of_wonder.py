import d20


def wonder(roll=1):
    if roll < 6:
        response = f"{roll}: You cast Slow."
    elif roll < 11:
        response = f"{roll}: You cast Faerie Fire."
    elif roll < 16:
        response = f"{roll}: You are Stunned until the start of your next turn, believing something awesome just " \
                   f"happened. "
    elif roll < 21:
        response = f"{roll}: You cast Gust of Wind."
    elif roll < 26:
        response = f"{roll}: You cast Detect Thoughts on the target you chose. If you didn't target a creature, " \
                   f"you instead take ({d20.roll('1d6')}) psychic damage. "
    elif roll < 31:
        response = f"{roll}: You cast Stinking Cloud."
    elif roll < 34:
        response = f"{roll}: Heavy rain falls in a 60-foot radius centered on the target. The area becomes lightly " \
                   f"obscured. The rain falls until the start of your next turn. "
    elif roll < 37:
        response = f"{roll}: An animal appears in the unoccupied space nearest the target. The animal isn't under " \
                   f"your control and acts as it normally would. Roll a d100 to determine which animal appears. "
        animal_roll = d20.roll('1d100')
        animal_roll_total = animal_roll.total
        if animal_roll_total < 26:
            animal = 'A Rhinoceros'
        elif animal_roll_total < 51:
            animal = 'An Elephant'
        elif animal_roll_total:
            animal = 'A Rat'
        return response + f"{animal_roll}: {animal} appears. See the Monster Manual for the animal's statistics."
    elif roll < 47:
        response = f"{roll}: You cast Lightning Bolt."
    elif roll < 50:
        response = f"{roll}: A cloud of 600 oversized butterflies fills a 30-foot radius centered on the target. The " \
                   f"area becomes heavily obscured. The butterflies remain for 10 minutes. "
    elif roll < 54:
        response = f"{roll}: You enlarge the target as if you had cast Enlarge/Reduce. If the target can't be " \
                   f"affected by that spell or if you didn't target a creature, you become the target. "
    elif roll < 59:
        response = f"{roll}: You cast Darkness."
    elif roll < 63:
        response = f"{roll}: Grass grows on the ground in a 60-foot radius centered on the target. If grass is " \
                   f"already there, it grows to ten times its normal size and remains overgrown for 1 minute. "
    elif roll < 66:
        response = f"{roll}: An object of the DM 's choice disappears into the Ethereal Plane. The object must be " \
                   f"neither worn nor carried, within 120 feet of the target, and no larger than 10 feet in any " \
                   f"dimension. "
    elif roll < 70:
        response = f"{roll}: You shrink yourself as if you had cast Enlarge/Reduce on yourself."
    elif roll < 80:
        response = f"{roll}: You cast Fireball."
    elif roll < 85:
        response = f"{roll}: You cast Invisibility on yourself."
    elif roll < 88:
        response = f"{roll}: Leaves grow from the target. If you chose a point in space as the target, leaves sprout " \
                   f"from the creature nearest to that point. Unless they are picked off, the leaves turn brown and " \
                   f"fall off after 24 hours. "
    elif roll < 91:
        response = f"{roll}: A stream of {d20.roll('1d4*10')} gems, each worth 1 gp, shoots from the wand's tip in a " \
                   f"line 30 feet long and 5 feet wide. Each gem deals 1 bludgeoning damage, and the total damage of " \
                   f"the gems is  divided equally among all creatures in the line. "
    elif roll < 96:
        response = f"{roll}: A burst of colorful shimmering light extends from you in a 30-foot radius. You and each " \
                   f"creature in the area that can see must succeed on a DC 15 Constitution saving throw or become " \
                   f"Blinded for 1 minute. A creature can repeat the saving throw at the end of each of its turns, " \
                   f"Ending the Effect on itself on a success. "
    elif roll < 98:
        response = f"{roll}: The target's skin turns bright blue for {d20.roll('1d10')} days. If you chose a point in " \
                   f"space, the creature nearest to that point is affected. "
    else:
        response = f"{roll}: If you targeted a creature, it must make a DC 15 Constitution saving throw. If you " \
                   f"didn't target a creature, you become the target and must make the saving throw. If the saving " \
                   f"throw fails by 5 or more, the target is instantly Petrified. On any other failed save, " \
                   f"the target is Restrained and begins to turn to stone. While Restrained in this way, the target " \
                   f"must repeat the saving throw at the end of its next turn, becoming Petrified on a failure or " \
                   f"Ending the Effect on a success. The petrification lasts until the target is freed by the Greater " \
                   f"Restoration spell or similar magic. "

    return response


if __name__ == '__main__':
    for x in range(1, 101):
        print(wonder(x))
