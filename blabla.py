    if zaal[randomNumber1].tijd19 = None:

        lijstRandom2 = []

        j = 0

        for j in range(29):
            lijstRandom2.append(j)

        # set a random number
        randomNumber2 = lijstRandom2[j]

        for i in range(len(vakken[randomNumber2])):

            if vakken[randomNumber2].hc1 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_hoorcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].hc1
                    vakken[randomNumber2].hc1 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].hc2 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_hoorcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].hc2
                    vakken[randomNumber2].hc2 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].hc3 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_hoorcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].hc3
                    vakken[randomNumber2].hc3 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].wc1 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_werkcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].wc1
                    vakken[randomNumber2].wc1 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].wc2 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_werkcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].wc2
                    vakken[randomNumber2].wc2 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].wc3 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_werkcollege))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].wc3
                    vakken[randomNumber2].wc3 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].p1 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p1
                    vakken[randomNumber2].p1 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].p2 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p2
                    vakken[randomNumber2].p2 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].p3 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p3
                    vakken[randomNumber2].p3 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].p4 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p4
                    vakken[randomNumber2].p4 = None
                    break
                else:
                    continue
            elif vakken[randomNumber2].p5 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p5
                    break
                else:
                    continue
            elif vakken[randomNumber2].p6 != None:
                if int(zaal[randomNumber1].max_capaciteit) >= int(vakken[randomNumber2].aantal_practica))
                    zaal[randomNumber1].tijd19 = vakken[randomNumber2].p6
                    break
                else:
                    continue
