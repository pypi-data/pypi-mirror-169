from pyenzyme import EnzymeMLDocument
from pyenzymekinetics import to_concentration, StandardCurve
import numpy as np

def abso_to_conc(
    enzmldoc: EnzymeMLDocument,
    standard_curve: StandardCurve, 
    reactant_id: str,
    blanc_data: bool = False,
    **kwargs
    ) -> EnzymeMLDocument:

    measurements_ids = list(enzmldoc.measurement_dict.keys())
    n_measurements = len(measurements_ids)
    n_replicates = len(enzmldoc.measurement_dict["m0"].species_dict["reactants"][reactant_id].replicates)
    n_data = len(enzmldoc.measurement_dict["m0"].species_dict["reactants"][reactant_id].replicates[0].data)
    time = enzmldoc.measurement_dict["m0"].species_dict["reactants"][reactant_id].replicates[0].time
    measurement_shape = (n_measurements ,n_replicates, n_data)

    datas = []
    meas_data = enzmldoc.exportMeasurementData()
    for id in measurements_ids:
        datas.append(meas_data[id]["data"][reactant_id].tolist())

    datas = np.array(datas).reshape(n_measurements*n_replicates, n_data)

    conc = to_concentration(standard_curve, datas)
    new_n_data = int(conc.size/n_measurements/n_replicates)
    new_shape = (n_measurements, n_replicates ,new_n_data)
    conc = conc.reshape(new_shape)

    for id, measurement_data in zip(measurements_ids, conc):
        enzmldoc.measurement_dict[id].global_time = time[:new_n_data]
        for i, replicate_data in zip(range(n_measurements), measurement_data):

            replicate = enzmldoc.measurement_dict[id].species_dict["reactants"][reactant_id].replicates[i]
            replicate.time = []
            replicate.data = []

            if blanc_data:
                replicate.data = [x-replicate_data[0] for x in list(replicate_data)]
            else:
                replicate.data = list(replicate_data)

            replicate.time = time[:new_n_data]
            replicate.is_calculated = True
            replicate.data_type = "conc"
            replicate.data_unit = standard_curve.concentration_unit

    return enzmldoc


if __name__ == "__main__":
    import numpy as np
    import pyenzyme as pe
    import pandas as pd
    from pyenzymekinetics import EnzymeKinetics
    enzmldoc = pe.EnzymeMLDocument.fromFile("/Users/maxhaussler/Dropbox/master_thesis/data/chantal/round7/a-glucosidase_inhibition.omex")

    df_reference = pd.read_excel("/Users/maxhaussler/Dropbox/master_thesis/data/chantal/round3/standard.xlsx",sheet_name="csv")
    standardcurve = StandardCurve(df_reference.conc.values, df_reference.abso.values, "mM", "p-NP")


    result = abso_to_conc(enzmldoc, standardcurve,"s1")
    #print(result)
    result.visualize()




