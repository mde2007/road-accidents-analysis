import pandas as pd

MISSING_RULES = {
    # ---------- COLLISION ----------
    "enhanced_collision_severity": {"na": [-1]},
    "local_authority_district": {"na": [-1]},
    "local_authority_ons_district": {"na": [-1]},
    "local_authority_highway": {"na": [-1]},
    "first_road_class": {"na": [-1]},
    "first_road_number": {"na": [-1]},
    "road_type": {"na": [-1], "unknown": [9], "normal": [1, 2, 3, 6, 7, 12]},
    "speed_limit": {"na": [-1], "unknown": [99], "normal": [20, 30, 40, 50, 60, 70]},
    "junction_detail_historic": {"na": [-1], "unknown": [99]},
    "junction_detail": {"na": [-1], "unknown": [99]},
    "junction_control": {"na": [-1], "unknown": [9]},
    "second_road_class": {"na": [-1], "unknown": [9]},
    "second_road_number": {"na": [-1]},
    "pedestrian_crossing_human_control_historic": {"na": [-1], "unknown": [9]},
    "pedestrian_crossing_physical_facilities_historic": {"na": [-1], "unknown": [9]},
    "pedestrian_crossing": {"na": [-1], "unknown": [99]},
    "light_conditions": {"na": [-1], "normal": [1, 4, 5, 6, 7]},
    "weather_conditions": {"na": [-1], "unknown": [9], "normal": [1, 2, 3, 4, 5, 6, 7, 8]},
    "road_surface_conditions": {"na": [-1], "unknown": [9], "normal": [1, 2, 3, 4, 5, 6, 7]},
    "special_conditions_at_site": {"na": [-1], "unknown": [9]},
    "carriageway_hazards_historic": {"na": [-1], "unknown": [9]},
    "carriageway_hazards": {"na": [-1], "unknown": [99]},
    "urban_or_rural_area": {"na": [-1], "normal": [1, 2, 3]},
    "did_police_officer_attend_scene_of_collision": {"na": [-1]},
    "did_police_officer_attend_scene_of_accident": {"na": [-1]},
    "trunk_road_flag": {"na": [-1]},
    # ---------- VEHICLE ----------
    "vehicle_type": {"na": [-1], "unknown": [99]},
    "towing_and_articulation": {"na": [-1], "unknown": [9]},
    "vehicle_manoeuvre_historic": {"na": [-1], "unknown": [99]},
    "vehicle_manoeuvre": {"na": [-1], "unknown": [99]},
    "vehicle_direction_from": {"na": [-1], "unknown": [9]},
    "vehicle_direction_to": {"na": [-1], "unknown": [9]},
    "vehicle_location_restricted_lane_historic": {"na": [-1], "unknown": [99]},
    "vehicle_location_restricted_lane": {"na": [-1], "unknown": [99]},
    "junction_location": {"na": [-1], "unknown": [9]},
    "skidding_and_overturning": {"na": [-1], "unknown": [9]},
    "hit_object_in_carriageway": {"na": [-1], "unknown": [99]},
    "vehicle_leaving_carriageway": {"na": [-1], "unknown": [9]},
    "hit_object_off_carriageway": {"na": [-1], "unknown": [99]},
    "first_point_of_impact": {"na": [-1], "unknown": [9]},
    "vehicle_left_hand_drive": {"na": [-1], "unknown": [9]},
    "journey_purpose_of_driver_historic": {"na": [-1], "unknown": [6]},
    "journey_purpose_of_driver": {"na": [-1], "unknown": [6]},
    "sex_of_driver": {"na": [-1], "unknown": [3]},
    "age_of_driver": {"na": [-1]},
    "age_band_of_driver": {"na": [-1]},
    "engine_capacity_cc": {"na": [-1]},
    "propulsion_code": {"na": [-1]},
    "generic_make_model": {"na": [-1]},
    "driver_imd_decile": {"na": [-1]},
    "driver_distance_banding": {"na": [-1]},
    # ---------- CASUALTY ----------
    "sex_of_casualty": {"na": [-1], "unknown": [9]},
    "age_of_casualty": {"na": [-1]},
    "age_band_of_casualty": {"na": [-1]},
    "enhanced_casualty_severity": {"na": [-1]},
    "pedestrian_location": {"na": [-1], "unknown": [10]},
    "pedestrian_movement": {"na": [-1], "unknown": [9]},
    "car_passenger": {"na": [-1], "unknown": [9]},
    "bus_or_coach_passenger": {"na": [-1], "unknown": [9]},
    "pedestrian_road_maintenance_worker": {"na": [-1], "unknown": [2]},
    "casualty_type": {"na": [-1], "unknown": [99]},
    "casualty_imd_decile": {"na": [-1]},
    "casualty_distance_banding": {"na": [-1]},
}


def replace_missing_values(dataframe, rules=MISSING_RULES):
    df = dataframe.copy()

    for col, values in rules.items():
        if col not in df.columns:
            continue

        df[col] = df[col].replace(values["na"], pd.NA)

    return df
