Write a python code that takes cloth image as input. write a script that identifies cloth type like shirt, jeans etc and cloth color by using appropriate machine learning model(s). Now, write a code that suggests possible top and bottom cloth based on,

- Mix of warm and cool colors with user's nuetral colors. (https://www.wikihow.com/Choose-Your-Best-Clothing-Colors)
- Mix of analogues colors
  (Analogous color matching involves combining two or three continuous shades on the color wheel for a striking and stylish look.
  )
- Monochrome style (formal wear - greys, blues, whites, and blacks, then progress to pastel undertones for other occasions)
- Contrasting Combination
- Complementry Combination (Red and green, violet and yellow, blue and orange)
- Soft Combination
- Mix of neutral and complementary colors
- manually match colors (https://nextlevelgents.com/easy-ways-to-match-clothes/) (https://color.adobe.com/create/color-wheel)
- User skin tone, outside weather, temperature, occasion etc.
  (If you are pale or yellow toned, opt for colors from the colder side of the palette, such as grey, navy blue, varying shades of green, aqua, emerald, burgundy, etc. If you have a deeper skin tone, you can pull off brighter or warmer shades of brown, coral, honey, gold, amber, taupe, etc. To look your best, select colors that complement your skin undertone.
  )
- Triadic color matching refers to the combination of colors that are equidistant from each other on the color wheel.

output cloth pair should also mention what technique was used to match respective pair.

step1

pair -
hair, scarf, glasses, top, bottom, shoes

write a Python code to detect objects like hair, sunglasses, top wear, bottom wear, shoes, and their colors from a given image.

write a Python code to detect objects like top wear, bottom wear of male and female gender from a given user's image.

cloth type and color detection

Cool and Warm colors

Warm | Cool
arouse or stimulate the viewer | calm and relax
Red, orange, yellow, brown | blue, purple, green

Nuetral colors
go with one cool or warm color, and leave everything else neutral.
black, white, brown, cream, grey and their shades, light blue, khaki, sand, biege

================================================
uvicorn main:app --reload


warm + nuetral
cool + nuetral
complementry + nuetral
is paired color analogues?
is paired color monochromatic?
is paired color complementry?
is paired color contrasting?

color harmony rule:
	analogous
	monochromatic
	Triadic
	complementry
	split complementry
	double split complementry
	square
	compound
	shades


is color nuetral?
is color warm/cool?
bright/muted in warm/cool

contrasting bold and active
Blue and orange in vibrant and energetic
black and white



SPA

user profile
add cloth
list closet


Backend

add cloth - remove background, resize, pre process, identify cloth type, generate color palette

Act as a full-stack developer. i want to create a pwa which has 3 pages.

1) upload image with camera/gallery
- this step will allow user to upload cloth image and back end should pre process this image and add it to user's closet

2) show closet to user
- show all/top/bottom wear to user based on selected filter

3) show matching cloth pair(s) of top and bottom wear based on cloth's color combination

There are multiple frontend/backend/fullstack frameworks which can be used to achieve this. Like Django, NextJS, VueJS, NestJS etc. Can you suggest a ideal framework(s) or tech stack that would be suitalbe for this use case? Also, elaborate on why suggested tech stack were chosen?

Please note that i would prefer to use python to pre process and classify cloth images.


