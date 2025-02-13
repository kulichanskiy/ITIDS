import * as fetcher from './databaseFetcher.js'

export async function getStationParametersByID(id) {
    const content = await fetcher.fetchStationByID(id);
    alert(`Station ID: ${id}
        Station name: ${content.station_name_en}
        French localisation: ${content.station_name_fr? content.station_name_fr : "None"}
        Zone: ${content.zone}
        Exit direction${content.exit_inbound !== content.exit_outbound ? `(Inbound/Outbound): ${content.exit_inbound}/${content.exit_outbound}` : `: ${content.exit_inbound}`}
        `);
}