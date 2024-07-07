init python:
    def customize_character(part, direction):
        global eye_brow
        global eye
        global nose
        global mouth
        global hair
        global category

        if direction == "right":
            if part == "eye_brow":
                if eye_brows.index(eye_brow) < len(eye_brows) - 1:
                    eye_brow = eye_brows[eye_brows.index(eye_brow) + 1]
                else:
                    eye_brow = eye_brows[0]
            if part == "eye":
                if eyes.index(eye) < len(eyes) - 1:
                    eye = eyes[eyes.index(eye) + 1]
                else:
                    eye = eyes[0]
            if part == "nose":
                if noses.index(nose) < len(noses) - 1:
                    nose = noses[noses.index(nose) + 1]
                else:
                    nose = noses[0]
            if part == "mouth":
                if mouths.index(mouth) < len(mouths) - 1:
                    mouth = mouths[mouths.index(mouth) + 1]
                else:
                    mouth = mouths[0]
            if part == "hair":
                if hairs.index(hair) < len(hairs) - 1:
                    hair = hairs[hairs.index(hair) + 1]
                else:
                    hair = hairs[0]
            if part == "category":
                if categories.index(category) < len(categories) - 1:
                    category = categories[categories.index(category) + 1]
                else:
                    category = categories[0]
                Show(character_customizer)
        elif direction == "left":
            if part == "eye_brow":
                if eye_brows.index(eye_brow) > 0:
                    eye_brow = eye_brows[eye_brows.index(eye_brow) - 1]
                else:
                    eye_brow = eye_brows[-1]
            if part == "eye":
                if eyes.index(eye) > 0:
                    eye = eyes[eyes.index(eye) - 1]
                else:
                    eye = eyes[-1]
            if part == "nose":
                if noses.index(nose) > 0:
                    nose = noses[noses.index(nose) - 1]
                else:
                    nose = noses[-1]
            if part == "mouth":
                if mouths.index(mouth) > 0:
                    mouth = mouths[mouths.index(mouth) - 1]
                else:
                    mouth = mouths[-1]
            if part == "hair":
                if hairs.index(hair) > 0:
                    hair = hairs[hairs.index(hair) - 1]
                else:
                    hair = hairs[-1]
            if part == "category":
                if categories.index(category) > 0:
                    category = categories[categories.index(category) - 1]
                else:
                    category = categories[-1]
                Show(character_customizer)

        renpy.retain_after_load()

    # def customize_character(part, direction):
    #     global hair
    #     global eye

    #     if direction == "right":
    #         if part == "hair":
    #             if hairs.index(hair) < len(hairs) - 1:
    #                 hair = hairs[hairs.index(hair) + 1]
    #             else:
    #                 hair = hairs[0]
    #         if part == "eye":
    #             if eyes.index(eye) < len(eyes) - 1:
    #                 eye = eyes[eyes.index(eye) + 1]
    #             else:
    #                 eye = eyes[0]
    #     elif direction == "left":
    #         if part == "hair":
    #             if hairs.index(hair) > 0:
    #                 hair = hairs[hairs.index(hair) - 1]
    #             else:
    #                 hair = hairs[-1]
    #         if part == "eye":
    #             if eyes.index(eye) > 0:
    #                 eye = eyes[eyes.index(eye) - 1]
    #             else:
    #                 eye = eyes[-1]
            


    #     renpy.retain_after_load()

    def customize_colors(part, color):
        global hair_color
        global eye_color
        global body
        global mouth_color
        global mouth_color_other

        if part == "hair":
            hair_color = color
        elif part == "eyes":
            eye_color = color
        elif part == "body":
            body = color
        elif part == "mouth":
            mouth_color = color
            if color == "pink":
                mouth_color_other = "brown"
            else:
                mouth_color_other = "pink" 
