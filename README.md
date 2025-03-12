# Quantum-Coherence-in-Microtubules

# Microtubule Quantum Coherence Simulation
I’m a self-taught coder diving into quantum effects in neural systems. This repo supports my pre-release paper "Microtubule Quantum Coherence at 40 Hz: Computational Evidence" (preprint link TBD—bioRxiv’s down, might try arXiv/OSF soon).

## Overview
- **Finding**: My simulations (GROMACS + QuTiP) show microtubules in brain cells can hold quantum coherence for 408 femtoseconds (fs) at 40 Hz, thanks to ordered water shielding (0.28 nm spacing, shielding factor 3.57 nm⁻¹).  
- **Why**: Could hint at how the brain works—sharing the core result now, full theory later after feedback.  

## Contents
- `gromacs_sim/`: GROMACS files (PDB 1TUB, topology, `.mdp` configs) and a script for a 1,000 ps run at 310 K.  
- `qutip_sim/`: QuTiP Python script modeling a two-level system hitting 408 fs coherence.  
- `data/`: RDF output (g(r) = 6.368876 at 0.28 nm) and coherence plot (1.0 ps run).  
- `paper/`: Trimmed PDF of the pre-release paper (once uploaded).  
- `LICENSE`: MIT License—see below.  
- `README.md`: You’re reading it!

## How to Run
1. **GROMACS**: Install GROMACS 2025.0 (CLANG64/MSYS2). Run `gromacs_sim/run.sh` after setup. Analyze with `gmx rdf -f md.xtc -s md.tpr -ref "Protein" -sel "SOL" -rmax 2.0 -bin 0.002 -norm number_density`.  
2. **QuTiP**: Install QuTiP 5.0.3. Run `qutip_sim/coherence.py` to see 408 fs coherence.  
3. **Output**: Check `data/` for RDF (water spacing) and coherence plots.

## Notes
- Replicates 40 Hz microtubule coherence—test it out!  
- This is a pre-release—full quantum consciousness ideas are still cooking. Hit me up on X [@yourhandle] for collab or questions.  
- For research only—don’t try anything wild without ethical review.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share the code—just give credit and don’t hold me liable. Paper and data are included under the same terms (CC BY 4.0 also works if you prefer for the text—your call!).

## Next Steps
- Awaiting preprint link (bioRxiv’s glitchy—might switch platforms).  
- Want feedback from neuro/quantum folks—run it and tell me what you think!