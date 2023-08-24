export function groupBy(data, key) {
    return data.reduce(
        (entryMap, e) => entryMap.set(e[key], [...entryMap.get(e[key]) || [], e]),
        new Map(),
    );
};