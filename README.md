# 😷 COVID-19: Exploring the Effectiveness of Wearing Masks

https://devpost.com/software/mcla/edit

## 💡 Inspiration
Ever since the beginning of the COVID-19 outbreak, there has been some resistance to wearing or not wearing a mask. Our group decided to create a simulation to predict the motion of the cough particles and how they are (or aren’t) impacted by the masks, to help visualize the impact and effectiveness of wearing them.

## 🏗️ What it does
To do so, we created an environment in python that would simulate the COVID-19 particles and droplets during and after coughing.

## ⚽ Physics
The particles were randomly created following the histogram of cough particle distribution (Duguid 1946) and the dispersion angle of the cough (J. Fluid Mech. (2014)) was also taken into account for the code. The amount of particles was calculated using the volume estimated by McCool 2006; Gupta et al. 2009; Park et al. 2010.

The droplets were separated in three cases: Large (>100µm), medium (100µm<d<10µm) and droplet nuclei (d<10µ).For the large particles, the droplets do not evaporate fast enough and the particles follow a projectile motion.

For the medium sized, the evaporation of the droplets makes this a problem of change in mass, and thus we use fluid evaporation of a spherically symmetric droplet and  conservation of momentum to calculate the change in velocity. The evaporation has a threshold of change in mass in which the new mass M-dm is (M-dm)<0.0997((10m)3/ 6 , and so the particles fall within the next category. That is represented by the particles that do not hit the floor.

The droplet nuclei has a radius so small that the water evaporates at an extremely fast rate, making the particles light enough to have its motion dictated by air flow. This was implemented on the code with gass motion on confined space. 

The scenarios were analyzed:
1- No mask (no filtration)
2- Surgical mask (filtration efficiency of 37% to 69%)
3- N95 (filtration efficiency of up to 95%)
The surgical mass creates a hot and humid space between the person and the mask which lowers the evaporation rates and makes it so that the droplets are easier to be kept from leaving to the outside
The N95 has some interesting physics behind it: the gaps between fibers are larger than all the particles it filters. The objective is not to make particles be blocked by their gap, but for them to be stuck to the fiber. 

This happens naturally for the larger droplets, but to make this happen to the smaller sized ones, two techniques are used: 

1. Multiple layers of fibers are used, and since the small droplets have an almost linear motion as they leave the mouth, about 100% of them are caught by the mask. 
2. Medium sized particles go through the air flow, and so the fibers are electricized to attract particles at a molecular level, creating a local change of potential that attracts them to the fiber and makes them leave the airflow and get stuck on the fibers, which filters up to 95% of them. 

Both masks will also impact the range of the motion, which becomes smaller since they have to go through a change of medium before getting outside.

## 👨‍💻 Challenges
On the programming side, the biggest challenge was the way the particles had to interact with the environment. There are a lot of edge cases that needed to be taken account of. Furthermore, a lot of movement variations had to be applied to particles during their movement. This meant we had to come up with a very dynamic code that updates often.

Physically speaking, a lot of the formulas that we needed to use were new to us. We spent a lot of time reading and learning about these equations in order to be able to use them.

## 🤔 Conclusion
The conclusion is clear: The masks help filter out particles and make their range smaller when they do pass through. They are extremely important in stopping the spread of coronavirus. 

## 📚 References
- DUGUID, J. P. 1946 The size and the duration of air-carriage of respiratory droplets and droplet-nuclei. J. Hyg. 44 (6), 471–14:22]
- J. Fluid Mech. (2014), vol. 745, pp. 537–563. cCambridge University Press 2014doi:10.1017/jfm.2014.88
- McCool 2006; Gupta et al. 2009; Park et al. 2010
- Molina, A., Vyas, P., Khlystov, N., Kumar, S., Kothari, A., Deriso, D., ... & Prakash, M. (2020). Project 1000 x 1000: Centrifugal melt spinning for distributed manufacturing of N95 filtering facepiece respirators. arXiv preprint arXiv:2004.13494.

## Suggestions? 🥺 👉 👈
Please comment to let us know what you think!


