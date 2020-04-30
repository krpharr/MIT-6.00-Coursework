# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab
import matplotlib.pyplot as plt
import time

#random.seed()

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
	"""
	Representation of a simple virus (does not model drug effects/resistance).
	"""
	
	def __init__(self, maxBirthProb, clearProb):
		"""
		Initialize a SimpleVirus instance, saves all parameters as attributes
		of the instance.        
		
		maxBirthProb: Maximum reproduction probability (a float between 0-1)        
		
		clearProb: Maximum clearance probability (a float between 0-1).
		"""
		self.maxBirthProb = maxBirthProb
		self.clearProb = clearProb
	def __str__(self):
		s = "%r\nmaxBirthProb: %f	clearProb: %f" %(self, self.maxBirthProb, self.clearProb)
		return s
	def doesClear(self):
		"""
		Stochastically determines whether this virus is cleared from the
		patient's body at a time step. 
		
		returns: Using a random number generator (random.random()), this method
		returns True with probability self.clearProb and otherwise returns
		False.
		"""
		if random.random() <= self.clearProb:
			#print self, "cleared"
			return True
		else: 
			return False
	
	def reproduce(self, popDensity):
		"""
		Stochastically determines whether this virus particle reproduces at a
		time step. Called by the update() method in the SimplePatient and
		Patient classes. The virus particle reproduces with probability
		self.maxBirthProb * (1 - popDensity).
		
		If this virus particle reproduces, then reproduce() creates and returns
		the instance of the offspring SimpleVirus (which has the same
		maxBirthProb and clearProb values as its parent).         
	
		popDensity: the population density (a float), defined as the current
		virus population divided by the maximum population.         
		
		returns: a new instance of the SimpleVirus class representing the
		offspring of this virus particle. The child should have the same
		maxBirthProb and clearProb values as this virus. Raises a
		NoChildException if this virus particle does not reproduce.               
		"""
		if random.random() <= (self.maxBirthProb * (1 - popDensity)):
			"""return children"""
			#print self, "reproduced."
			return SimpleVirus(self.maxBirthProb, self.clearProb)
		else: raise NoChildException()

class SimplePatient(object):
	"""
	Representation of a simplified patient. The patient does not take any drugs
	and his/her virus populations have no drug resistance.
	"""
	
	def __init__(self, viruses, maxPop):
		"""
		Initialization function, saves the viruses and maxPop parameters as
		attributes.
	
		viruses: the list representing the virus population (a list of
		SimpleVirus instances)
		
		maxPop: the  maximum virus population for this patient (an integer)
		"""
		self.viruses = viruses
		self.maxPop = maxPop
	def __str__(self):
                s = "%r\n" % self
		s += "Number of virus cells: %d		maxPop: %d\n" %(len(self.viruses), self.maxPop)
		return s
	def getTotalPop(self):
		"""
		Gets the current total virus population. 
	
		returns: The total virus population (an integer)
		"""
		return len(self.viruses)       
	
	def update(self):
		"""
		Update the state of the virus population in this patient for a single
		time step. update() should execute the following steps in this order:
	
		- Determine whether each virus particle survives and updates the list
		  of virus particles accordingly.
	
		- The current population density is calculated. This population density
		  value is used until the next call to update() 
	
		- Determine whether each virus particle should reproduce and add
		  offspring virus particles to the list of viruses in this patient.                    
	
		returns: the total virus population at the end of the update (an
		integer)
		"""
		newcolony = []
		for i,v in reversed( list( enumerate(self.viruses))):
			if v.doesClear():
				self.viruses.pop(i)
		print "Total Polulation:", self.getTotalPop()
		popDensity = float(self.getTotalPop())/float(self.maxPop)
		print "Density:", popDensity
		for v in self.viruses:
			try:self.viruses.append(v.reproduce(popDensity))
			except NoChildException:
				continue
		return self.getTotalPop()
			

##
##v = []			
##for i in range(0, 10):
##        v.append(SimpleVirus(0.1, 0.05))
##patient = SimplePatient(v, 1000)
##print patient
##for i in range(0, 100):
##    patient.update()
##    print patient
#
# PROBLEM 2
#

def problem2():
	"""
	Run the simulation and plot the graph for problem 2 (no drugs are used,
	viruses do not have any drug resistance).    
	
	Instantiates a patient, runs a simulation for 300 timesteps, and plots the
	total virus population as a function of time.    
	"""
	v = []			
	for i in range(0, 10):
		v.append(SimpleVirus(0.1, 0.05))
	patient = SimplePatient(v, 1000)
	print patient
	
	virus_population = []
	timestep = []
	for i in range(0, 300):
		virus_population.append(patient.update())
		timestep.append(i+1)

	plt.plot(timestep, virus_population)
	plt.axis([1, 300, 0, 800])
	plt.title('No drugs used on patient, viruses have no drug resistance.')
	plt.xlabel('Timesteps')
	plt.ylabel('Virus Population')
	plt.show()
	
#problem2()
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
    def __str__(self):
        s = ""
        s += SimpleVirus.__str__(self)
        s += "  mutProb: %f\n" % self.mutProb
        for d in self.resistances:
            s += "%s: %s\n" %(d, self.resistances[d])
        return s
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        #if len(activeDrugs):resist_any = False
        #else: resist_any = True 
        #for drug in activeDrugs:
            #if self.getResistance(drug):
                ##print "resists ", drug
                #resist_any = True
        ##print "resist_any: ", resist_any
        #if resist_any:
        resist_all = True 
        for drug in activeDrugs:
            if self.getResistance(drug) == False:
                #print "resists ", drug
                resist_all = False
        #print "resist_any: ", resist_any
        if resist_all:
            #print "self.maxBirthProb * (1 - popDensity)", self.maxBirthProb * (1 - popDensity)
            if random.random() <= (self.maxBirthProb * (1 - popDensity)):
                """return children"""
                child_resistances = {}
                for drug in self.resistances:
                    if random.random() <= self.mutProb: #mutate and reverse resistance to drug
                        if self.resistances[drug]:child_resistances[drug] = False
                        else: child_resistances[drug] = True
                    else:
                        child_resistances[drug] = self.resistances[drug]
                return ResistantVirus(self.maxBirthProb, self.clearProb, child_resistances, self.mutProb)
            else: raise NoChildException()
        else: raise NoChildException()

#############test class#########################
##v = {'a':True, 'b':False}
##r = []
##for i in range(0, 10):
##    r.append(ResistantVirus(0.1,0.05, v, 0.005))
##d = []
##r2 = []
##for i in range(0, 10):
##    try:
##        r2.append(r[i].reproduce(100/1000, d))
##    except NoChildException:
##        continue
##for i in r2:
##    print i

            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes self.meds, the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.meds = []
    def __str__(self):
        s = ""
        s += SimplePatient.__str__(self)
        s += "Resistant population: %i" %self.getResistPop(self.meds)
        s += "\nCurrent medications: "
        for med in self.meds:
            s += "%s \t" %med
        return s
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        print self, "taking ", newDrug
        self.meds.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.meds
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        population = 0
        for v in self.viruses:
            resist_all = True
            for drug in drugResist:
                if not v.getResistance(drug):
                    resist_all = False
            if resist_all: population += 1
        return population

    def update(self):
		"""
		Update the state of the virus population in this patient for a single
		time step. update() should execute these actions in order:
	
		- Determine whether each virus particle survives and update the list of 
		  virus particles accordingly
		  
		- The current population density is calculated. This population density
		  value is used until the next call to update().
	
		- Determine whether each virus particle should reproduce and add
		  offspring virus particles to the list of viruses in this patient. 
		  The listof drugs being administered should be accounted for in the
		  determination of whether each virus particle reproduces. 
	
		returns: the total virus population at the end of the update (an
		integer)
		"""
		for i,v in reversed( list( enumerate(self.viruses))):
			if v.doesClear():
				self.viruses.pop(i)
		popDensity = float(self.getTotalPop())/float(self.maxPop)
		for v in self.viruses:
			try:self.viruses.append(v.reproduce(popDensity, self.meds))
			except NoChildException:
				continue
		return self.getTotalPop()

#############test class#########################
##v = {'a':True, 'b':False}
##r = []
##for i in range(0, 10):
##    r.append(ResistantVirus(0.1,0.05, v, 0.005))
##d = []
##r2 = []
##for i in range(0, 10):
##    try:
##        r2.append(r[i].reproduce(100/1000, d))
##    except NoChildException:
##        continue
##for i in r2:
##    print i
##
##p = Patient(r, 1000)
##print p
##p.update()
##print p
##p.addPrescription('b')
##p.update()
##print p


#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    v = []			
    for i in range(0, 100):
            v.append(ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005))
    patient = Patient(v, 1000)
    print patient	
    
    population = []
    guttagonol_resistant = []
    timestep = []
    drug_resist_timestep = []
    for i in range(0, 150):
            population.append(patient.update())
            timestep.append(i+1)
    patient.addPrescription('guttagonol')
    for i in range(150, 300):
            population.append(patient.update())
            guttagonol_resistant.append(patient.getResistPop(['guttagonol']))
            timestep.append(i)
            drug_resist_timestep.append(i+1)

    plt.plot(timestep, population,drug_resist_timestep, guttagonol_resistant)
    plt.axis([1, 300, 1, 800])
    plt.title('Total virus population vs. time \n guttagonol-resistant virus population vs. time')
    plt.xlabel('Timesteps')
    plt.ylabel('Virus Populations')
    plt.show()

#problem4()

#
# PROBLEM 5
#

def ansQuest5(numSteps, numTrials):  #numTrials == numPatients
	population = []
	for trial in range(0, numTrials):
		viruses = []			
		for i in range(0, 100):
				viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005))
		patient = Patient(viruses, 1000)
		print trial, "of ", numTrials, " Patient ID:", patient
		for i in range(0, numSteps):
			patient.update()
		patient.addPrescription('guttagonol')
		#150 steps after treatment
		for i in range(0, 150): 
				patient.update()
		population.append(patient.getTotalPop())
		print patient
		print population
	return numSteps, population
	
def problem5():
	"""
	Runs simulations and make histograms for problem 5.
	
	Runs multiple simulations to show the relationship between delayed treatment
	and patient outcome.
	
	Histograms of final total virus populations are displayed for delays of 300,
	150, 75, 0 timesteps (followed by an additional 150 timesteps of
	simulation).    
	"""
	startTime = time.time()
	trialResults = []
	trialResults.append(ansQuest5(300, 55))
	trialResults.append(ansQuest5(150, 55))
	trialResults.append(ansQuest5(75, 55))
	trialResults.append(ansQuest5(0, 55))
	endTime = time.time()
	print "Crunch time:%.4f" % ((endTime-startTime)/60)	
	print trialResults
	f = 0
	for r in trialResults:
		n = r[0]
		pylab.figure(f+1)
		pylab.hist(r[1])
		pylab.xlabel('Virus Population')
		pylab.ylabel('Number Patients')
		s = "Total virus population administering Guttagonol after %i timesteps" %n
		pylab.title(s)
		f += 1
	pylab.show()
           
#
# PROBLEM 6
#

def ansQuest6(numSteps, numTrials): 
	population = []
	for trial in range(0, numTrials):
		viruses = []			
		for i in range(0, 100):
				viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005))
		patient = Patient(viruses, 1000)
		print trial, "of ", numTrials, " Patient ID:", patient
		for i in range(0, 150): #150 steps before gutagonol
			patient.update()
		patient.addPrescription('guttagonol')
		for i in range(0, numSteps):
			patient.update()
		patient.addPrescription('grimpex')
		#150 steps after treatment
		for i in range(0, 150): 
				patient.update()
		population.append(patient.getTotalPop())
		print patient
		print population
	return numSteps, population

	
def test6():
    """
    """
    v = []			
    for i in range(0, 100):
            v.append(ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005))
    patient = Patient(v, 1000)
    print patient	
    
    population = []
    guttagonol_resistant = []
    grimpex_resistant = []
    timestep = []
    guttagonol_resist_timestep = []
    grimpex_resist_timestep = []
    for i in range(0, 200):
            population.append(patient.update())
            timestep.append(i+1)
    patient.addPrescription('guttagonol')
    for i in range(200, 250):
            population.append(patient.update())
            guttagonol_resistant.append(patient.getResistPop(['guttagonol']))
            timestep.append(i+1)
            guttagonol_resist_timestep.append(i+1)
    patient.addPrescription('grimpex')
    for i in range(250, 300):
            population.append(patient.update())
            guttagonol_resistant.append(patient.getResistPop(['guttagonol']))
            grimpex_resistant.append(patient.getResistPop(['grimpex']))
            timestep.append(i+1)
            guttagonol_resist_timestep.append(i+1)
            grimpex_resist_timestep.append(i+1)

    plt.plot(timestep, population,guttagonol_resist_timestep, guttagonol_resistant, grimpex_resist_timestep, grimpex_resistant)
    plt.axis([1, 300, 1, 800])
    plt.title('Total virus population vs. time \n guttagonol and grimpex resistant virus population vs. time')
    plt.xlabel('Timesteps')
    plt.ylabel('Virus Populations')
    plt.show()



def problem6():
	"""
	Runs simulations and make histograms for problem 6.
	
	Runs multiple simulations to show the relationship between administration
	of multiple drugs and patient outcome.
	
	Histograms of final total virus populations are displayed for lag times of
	150, 75, 0 timesteps between adding drugs (followed by an additional 150
	timesteps of simulation).
	"""
	startTime = time.time()
	trialResults = []
	trialResults.append(ansQuest6(300, 30))
	trialResults.append(ansQuest6(150, 30))
	trialResults.append(ansQuest6(75, 30))
	trialResults.append(ansQuest6(0, 30))
	endTime = time.time()
	print "Crunch time:%.4f" % ((endTime-startTime)/60)	
	print trialResults
	f = 0
	pylab.figure()
	s = ""
	pylab.title(s)
	for r in trialResults:
		n = r[0]
		pylab.figure(f+1)
		pylab.hist(r[1])
		numCured = 0
		for p in r[1]:
			if p <= 50:
				numCured += 1
		percentCured = 100 * (float(numCured) / float(len(r[1])))
		pylab.xlabel('Virus Population')
		pylab.ylabel('Number Patients')
		s = "150 steps - Guttagonol - %i steps - Grimpex - 150 steps %i%% cured" %(n, percentCured)
		pylab.title(s)
		f += 1
	pylab.show()

#
# PROBLEM 7
#

def ansQuest7(numSteps, numTrials): 
	def getAvg(pop):
		"""inline - returns list of average population totals in pop[]"""
		t = 0
		total_steps = len(pop)
		for i in xrange(0, len(pop)):
			t += pop[i]
		avg = t / len(pop)
		return avg
		
	population_totals = []
	resist_pop_totals = []
	guttagonol_resit_pop_totals = []
	grimpex_resit_pop_totals = []
	for trial in xrange(0, numTrials):
		viruses = []	
		population = []		
		resist_pop = []
		guttagonol_resist = []
		grimpex_resist = []
		for i in xrange(0, 100):
				viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005))
		patient = Patient(viruses, 1000)
		print trial, "of ", numTrials, " Patient ID:", patient
		for i in xrange(0, 150): #150 steps before gutagonol
			population.append(patient.update())
			resist_pop.append(patient.getResistPop(['guttagonol', 'grimpex']))
			guttagonol_resist.append(patient.getResistPop("guttagonol"))
			grimpex_resist.append(patient.getResistPop("grimpex"))
		patient.addPrescription('guttagonol')
		for i in xrange(0, numSteps):
			population.append(patient.update())
			resist_pop.append(patient.getResistPop(['guttagonol', 'grimpex']))
			guttagonol_resist.append(patient.getResistPop("guttagonol"))
			grimpex_resist.append(patient.getResistPop("grimpex"))
		patient.addPrescription('grimpex')
		#150 steps after treatment
		for i in xrange(0, 150): 
			population.append(patient.update())
			resist_pop.append(patient.getResistPop(['guttagonol', 'grimpex']))
			guttagonol_resist.append(patient.getResistPop("guttagonol"))
			grimpex_resist.append(patient.getResistPop("grimpex"))
		population_totals.append(population)
		resist_pop_totals.append(resist_pop)
		guttagonol_resit_pop_totals.append(guttagonol_resist)
		grimpex_resit_pop_totals.append(grimpex_resist)
		print patient
	avg_population = getAvg(population_totals)
	avg_resist = getAvg(resist_pop_totals)
	avg_guttagonol_resist = getAvg(guttagonol_resit_pop_totals)
	avg_grimpex_resist = getAvg(grimpex_resit_pop_totals)

	return avg_population, avg_resist, avg_guttagonol_resist, avg_grimpex_resist

     
def problem7():
	"""
	Run simulations and plot graphs examining the relationship between
	administration of multiple drugs and patient outcome.
	
	Plots of total and drug-resistant viruses vs. time are made for a
	simulation with a 300 time step delay between administering the 2 drugs and
	a simulations for which drugs are administered simultaneously.        
	"""
	total_pop, total_resistant, guttagonol_resistant, grimpex_resistant = ansQuest7(300, 1)
	timesteps = []
	for i in xrange(0, len(total_pop)):
		timesteps.append(i+1)
		
	print total_pop
	#plt.figure()
	#plt.plot(timesteps, total_pop)
	#plt.plot(timesteps, total_resistant)
	#plt.plot(timesteps, guttagonol_resistant)
	#plt.plot(timesteps, grimpex_resistant)
	#plt.legend([total_pop, total_resistant, guttagonol_resistant, grimpex_resistant], ["Total Population", "Total Resistant Population", "Guttagonol Resistant", "Grimpex Resistant"])
	#plt.axis([1, timesteps, 1, 600])
	#plt.title('')
	#plt.xlabel('Timesteps')
	#plt.ylabel('Virus Populations')
	#plt.show()
	
		
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#problem2()
#problem4()
#problem5()
#problem6()
problem7()
#test6()
